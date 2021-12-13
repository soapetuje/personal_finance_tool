from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import NewProfile, Filter, Base_Currency
from .models import Profile, User, Price
import requests, json, os
from datetime import date
from scipy import stats
from decimal import Decimal



# Create your views here.
# Checking if IEX token is set
token = os.environ.get("EXCHANGE_RATE_KEY")
if not token:
    raise RuntimeError("EXCHANGE_RATE_KEY not set")



def price():
    today = date.today()
    price_pairs, made = Price.objects.get_or_create(
            created = 'Y'
        )
    # check if model was created
    if made:
        
        response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={token}")
        # price_dictionary = json.loads(response.text)
        
        # rates = price_dictionary['rates']
        price_pairs.response = response.text
        

    else:
        # check if one day has pass since updated
        last_updated = price_pairs.updated
        delta = today - last_updated

        if delta.days:
            # if 1 day has passed get latest prices
            response = requests.get(f"http://api.exchangeratesapi.io/v1/latest?access_key={token}")
            price_pairs.response = response.text
            

            
        
    price_pairs.save()
    


def index(request):
    price()
    price_model = Price.objects.get(created='Y')

    return render(request, "personalfinance/index.html")

def rates(request):
    # Getting price information
    price()
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    current_date = json.loads(price_model.response)['date']

    symbols = {"AED":"United Arab Emirates Dirham","AFN":"Afghan Afghani","ALL":"Albanian Lek","AMD":"Armenian Dram","ANG":"Netherlands Antillean Guilder","AOA":"Angolan Kwanza","ARS":"Argentine Peso","AUD":"Australian Dollar","AWG":"Aruban Florin","AZN":"Azerbaijani Manat","BAM":"Bosnia-Herzegovina Convertible Mark","BBD":"Barbadian Dollar","BDT":"Bangladeshi Taka","BGN":"Bulgarian Lev","BHD":"Bahraini Dinar","BIF":"Burundian Franc","BMD":"Bermudan Dollar","BND":"Brunei Dollar","BOB":"Bolivian Boliviano","BRL":"Brazilian Real","BSD":"Bahamian Dollar","BTC":"Bitcoin","BTN":"Bhutanese Ngultrum","BWP":"Botswanan Pula","BYN":"New Belarusian Ruble","BYR":"Belarusian Ruble","BZD":"Belize Dollar","CAD":"Canadian Dollar","CDF":"Congolese Franc","CHF":"Swiss Franc","CLF":"Chilean Unit of Account (UF)","CLP":"Chilean Peso","CNY":"Chinese Yuan","COP":"Colombian Peso","CRC":"Costa Rican Col\u00f3n","CUC":"Cuban Convertible Peso","CUP":"Cuban Peso","CVE":"Cape Verdean Escudo","CZK":"Czech Republic Koruna","DJF":"Djiboutian Franc","DKK":"Danish Krone","DOP":"Dominican Peso","DZD":"Algerian Dinar","EGP":"Egyptian Pound","ERN":"Eritrean Nakfa","ETB":"Ethiopian Birr","EUR":"Euro","FJD":"Fijian Dollar","FKP":"Falkland Islands Pound","GBP":"British Pound Sterling","GEL":"Georgian Lari","GGP":"Guernsey Pound","GHS":"Ghanaian Cedi","GIP":"Gibraltar Pound","GMD":"Gambian Dalasi","GNF":"Guinean Franc","GTQ":"Guatemalan Quetzal","GYD":"Guyanaese Dollar","HKD":"Hong Kong Dollar","HNL":"Honduran Lempira","HRK":"Croatian Kuna","HTG":"Haitian Gourde","HUF":"Hungarian Forint","IDR":"Indonesian Rupiah","ILS":"Israeli New Sheqel","IMP":"Manx pound","INR":"Indian Rupee","IQD":"Iraqi Dinar","IRR":"Iranian Rial","ISK":"Icelandic Kr\u00f3na","JEP":"Jersey Pound","JMD":"Jamaican Dollar","JOD":"Jordanian Dinar","JPY":"Japanese Yen","KES":"Kenyan Shilling","KGS":"Kyrgystani Som","KHR":"Cambodian Riel","KMF":"Comorian Franc","KPW":"North Korean Won","KRW":"South Korean Won","KWD":"Kuwaiti Dinar","KYD":"Cayman Islands Dollar","KZT":"Kazakhstani Tenge","LAK":"Laotian Kip","LBP":"Lebanese Pound","LKR":"Sri Lankan Rupee","LRD":"Liberian Dollar","LSL":"Lesotho Loti","LTL":"Lithuanian Litas","LVL":"Latvian Lats","LYD":"Libyan Dinar","MAD":"Moroccan Dirham","MDL":"Moldovan Leu","MGA":"Malagasy Ariary","MKD":"Macedonian Denar","MMK":"Myanma Kyat","MNT":"Mongolian Tugrik","MOP":"Macanese Pataca","MRO":"Mauritanian Ouguiya","MUR":"Mauritian Rupee","MVR":"Maldivian Rufiyaa","MWK":"Malawian Kwacha","MXN":"Mexican Peso","MYR":"Malaysian Ringgit","MZN":"Mozambican Metical","NAD":"Namibian Dollar","NGN":"Nigerian Naira","NIO":"Nicaraguan C\u00f3rdoba","NOK":"Norwegian Krone","NPR":"Nepalese Rupee","NZD":"New Zealand Dollar","OMR":"Omani Rial","PAB":"Panamanian Balboa","PEN":"Peruvian Nuevo Sol","PGK":"Papua New Guinean Kina","PHP":"Philippine Peso","PKR":"Pakistani Rupee","PLN":"Polish Zloty","PYG":"Paraguayan Guarani","QAR":"Qatari Rial","RON":"Romanian Leu","RSD":"Serbian Dinar","RUB":"Russian Ruble","RWF":"Rwandan Franc","SAR":"Saudi Riyal","SBD":"Solomon Islands Dollar","SCR":"Seychellois Rupee","SDG":"Sudanese Pound","SEK":"Swedish Krona","SGD":"Singapore Dollar","SHP":"Saint Helena Pound","SLL":"Sierra Leonean Leone","SOS":"Somali Shilling","SRD":"Surinamese Dollar","STD":"S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra","SVC":"Salvadoran Col\u00f3n","SYP":"Syrian Pound","SZL":"Swazi Lilangeni","THB":"Thai Baht","TJS":"Tajikistani Somoni","TMT":"Turkmenistani Manat","TND":"Tunisian Dinar","TOP":"Tongan Pa\u02bbanga","TRY":"Turkish Lira","TTD":"Trinidad and Tobago Dollar","TWD":"New Taiwan Dollar","TZS":"Tanzanian Shilling","UAH":"Ukrainian Hryvnia","UGX":"Ugandan Shilling","USD":"United States Dollar","UYU":"Uruguayan Peso","UZS":"Uzbekistan Som","VEF":"Venezuelan Bol\u00edvar Fuerte","VND":"Vietnamese Dong","VUV":"Vanuatu Vatu","WST":"Samoan Tala","XAF":"CFA Franc BEAC","XAG":"Silver (troy ounce)","XAU":"Gold (troy ounce)","XCD":"East Caribbean Dollar","XDR":"Special Drawing Rights","XOF":"CFA Franc BCEAO","XPF":"CFP Franc","YER":"Yemeni Rial","ZAR":"South African Rand","ZMK":"Zambian Kwacha (pre-2013)","ZMW":"Zambian Kwacha","ZWL":"Zimbabwean Dollar"}

    ex_rates = {}
    if request.method == 'POST':
        # User wants to modify the base currency
        form = Base_Currency(request.POST)

        if form.is_valid():
            current_currency = form.cleaned_data['base_currency']
            for key in price_dictionary:
                # Logic for decimal places
                if key != "BTC":
                    ex_rates[key] = [symbols[key], round(price_dictionary[key]/price_dictionary[current_currency],2)]
                else:
                    ex_rates[key] = [symbols[key], round(price_dictionary[key]/price_dictionary[current_currency],8)]
            base_currency = Base_Currency(initial={"base_currency": current_currency})
            return render(request, "personalfinance/rates.html", {
                "date": current_date,
                "ex_rates": ex_rates,
                "form": form
            })
    else:
        for key in price_dictionary:
            if key != "BTC":
                ex_rates[key] = [symbols[key], round(price_dictionary[key],2)]
            else:
                ex_rates[key] = [symbols[key], round(price_dictionary[key],8)]
        
        base_currency = Base_Currency()

        return render(request, "personalfinance/rates.html", {
            "date": current_date,
            "ex_rates": ex_rates,
            "form": base_currency
        })
    

@login_required
def dashboard(request):
    price()
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']

    user_profile = Profile.objects.get(author=request.user)
    all_users = Profile.objects.all()
    all_income = []
    all_assets = []
    all_debts = []
    
    for user in all_users:
        # Converting back to Euro
        conversion = Decimal(price_dictionary[user.currency])
        all_income.append(user.income/conversion)
        all_assets.append(user.assets/conversion)
        all_debts.append(user.debts/conversion)
        
    all_net_worth = [all_assets[i] - all_debts[i] for i in range(len(all_debts))]

    all_income.sort()
    all_assets.sort()
    all_debts.sort()
    all_net_worth.sort()

    
    # from https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile
    income_percentiles = dict(zip(all_income,(stats.rankdata(all_income, 'min')-1)/len(all_income)*100))
    asset_percentiles = dict(zip(all_assets,(stats.rankdata(all_assets, 'min')-1)/len(all_assets)*100))
    debt_percentiles = dict(zip(all_debts,(stats.rankdata(all_debts, 'min')-1)/len(all_debts)*100))
    net_worth_percentiles = dict(zip(all_net_worth,(stats.rankdata(all_net_worth, 'min')-1)/len(all_net_worth)*100))
    
    conversion = Decimal(price_dictionary[user_profile.currency])
    income_percentile = int(income_percentiles[user_profile.income/conversion])
    asset_percentile = int(asset_percentiles[user_profile.assets/conversion])
    debt_percentile = int(debt_percentiles[user_profile.debts/conversion])
    net_worth_percentile = int(net_worth_percentiles[user_profile.assets/conversion - user_profile.debts/conversion])

    # determine correct suffix to use
    suffixes = {0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th'}
    income_suffix = suffixes[income_percentile % 10]
    asset_suffix = suffixes[asset_percentile % 10]
    debt_suffix = suffixes[debt_percentile % 10]
    net_worth_suffix = suffixes[net_worth_percentile % 10]
    
    currency = user_profile.currency
    income = user_profile.income
    assets = user_profile.assets
    debts = user_profile.debts
    net_worth = assets - debts

    filter_fields = Filter(initial={"currency": currency})
    no_of_users = len(all_users)

    if currency == 'BTC':
        return render(request, "personalfinance/dashboard.html", {
            "currency": currency,
            "income": f'{income:.8f}', "assets": f'{assets:.8f}', "debts": f'{debts:.8f}',
            "net_worth": f'{net_worth:.8f}', "income_percentile": income_percentile,
            "asset_percentile": asset_percentile, "debt_percentile": debt_percentile,
            "net_worth_percentile": net_worth_percentile,
            "filter_fields": filter_fields,
            "income_suffix": income_suffix,
            "asset_suffix": asset_suffix,
            "debt_suffix": debt_suffix,
            "net_worth_suffix": net_worth_suffix,
            "no_of_users": no_of_users
        })
    else:
        return render(request, "personalfinance/dashboard.html", {
            "currency": currency,
            "income": f'{income:.2f}', "assets": f'{assets:.2f}', "debts": f'{debts:.2f}',
            "net_worth": f'{net_worth:.2f}', "income_percentile": income_percentile,
            "asset_percentile": asset_percentile, "debt_percentile": debt_percentile,
            "net_worth_percentile": net_worth_percentile,
            "filter_fields": filter_fields,
            "income_suffix": income_suffix,
            "asset_suffix": asset_suffix,
            "debt_suffix": debt_suffix,
            "net_worth_suffix": net_worth_suffix,
            "no_of_users": no_of_users
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "personalfinance/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "personalfinance/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "personalfinance/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError:
            return render(request, "personalfinance/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("profile"))
    else:
        return render(request, "personalfinance/register.html")

@login_required
def profile(request):
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    if request.method == 'POST':

        form = NewProfile(request.POST)

        if form.is_valid():

            age_group = form.cleaned_data['age_group']
            ethnicity = form.cleaned_data['ethnicity']
            race = form.cleaned_data['race']
            education = form.cleaned_data['education']
            currency = form.cleaned_data['currency']
            income = form.cleaned_data['income']
            assets = form.cleaned_data['assets']
            debts = form.cleaned_data['debts']


            profile, created = Profile.objects.get_or_create(
                author = request.user
            )
            profile.age_group = age_group
            profile.ethnicity = ethnicity
            profile.race = race
            profile.education = education
            profile.currency = currency
            profile.income = income
            profile.assets = assets
            profile.debts = debts
            profile.save()
            return HttpResponseRedirect(reverse("dashboard"))
    else:
        try:
            user_profile = Profile.objects.get(author=request.user)
        except:
            user_profile = None
        if user_profile:
            income = user_profile.income
            assets = user_profile.assets
            debts = user_profile.debts
            
            profile_data = {"ethnicity": user_profile.ethnicity,
            "education": user_profile.education, "race": user_profile.race, "currency": user_profile.currency,
            "income": income, "assets": assets, "debts": debts, "age_group": user_profile.age_group}
            form =NewProfile(initial=profile_data)
        else:
            form = NewProfile()
            return render(request, "personalfinance/first_profile.html", {"form": form})
        return render(request, "personalfinance/profile.html", {
            "form": form
        })

@csrf_exempt
@login_required
def update_currency(request):
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    # make sure request was POST
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)
    # print(data)
    # determine if the request was sent from dashboard (>5 fields) or profile
    if len(data) > 5:
        new_income = float(data["income"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]
        new_assets = float(data["assets"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]
        new_liabilities = float(data["debts"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]
        new_net_worth = float(data["net_worth"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]

        if data["new_currency"] == 'BTC':
            new_data = {"new_income": f'{new_income:.8f}', "new_assets": f'{new_assets:.8f}',
                "new_liabilities": f'{new_liabilities:.8f}', "new_net_worth": f'{new_net_worth:.8f}',
            }
        else:
            new_data = {"new_income": f'{new_income:.2f}', "new_assets": f'{new_assets:.2f}',
                "new_liabilities": f'{new_liabilities:.2f}', "new_net_worth": f'{new_net_worth:.2f}',
            }
    else:
        new_income = float(data["income"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]
        new_assets = float(data["assets"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]
        new_liabilities = float(data["debts"]) * price_dictionary[data["new_currency"]]/price_dictionary[data["old_currency"]]

        if data["new_currency"] == 'BTC':
            new_data = {"new_income": f'{new_income:.8f}', "new_assets": f'{new_assets:.8f}',
                "new_liabilities": f'{new_liabilities:.8f}'
            }
        else:
            new_data = {"new_income": f'{new_income:.2f}', "new_assets": f'{new_assets:.2f}',
                "new_liabilities": f'{new_liabilities:.2f}'
            }
    return JsonResponse(new_data, status=201)

@csrf_exempt
@login_required
def filter_education(request):
    price()
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    selected_education = data['education']

    user_profile = Profile.objects.get(author=request.user)
    all_income = []
    all_assets = []
    all_debts = []
    hide_message = 0

    # if user selected 'All' or not
    if selected_education == 'AL':
        all_users = Profile.objects.all()
        hide_message = 1
        no_of_users = len(all_users)
    else:
        all_users = Profile.objects.filter(education=selected_education)
        if user_profile not in all_users:
            no_of_users = len(all_users) + 1
        else:
            no_of_users = len(all_users)
        
    for user in all_users:
        if user.author != request.user:
            conversion = Decimal(price_dictionary[user.currency])
            all_income.append(user.income/conversion)
            all_assets.append(user.assets/conversion)
            all_debts.append(user.debts/conversion)
    
    conversion = Decimal(price_dictionary[user_profile.currency])
    all_income.append(user_profile.income/conversion)
    all_assets.append(user_profile.assets/conversion)
    all_debts.append(user_profile.debts/conversion)

    all_net_worth = [all_assets[i] - all_debts[i] for i in range(len(all_debts))]

    all_income.sort()
    all_assets.sort()
    all_debts.sort()
    all_net_worth.sort()

    # from https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile
    income_percentiles = dict(zip(all_income,(stats.rankdata(all_income, 'min')-1)/len(all_income)*100))
    asset_percentiles = dict(zip(all_assets,(stats.rankdata(all_assets, 'min')-1)/len(all_assets)*100))
    debt_percentiles = dict(zip(all_debts,(stats.rankdata(all_debts, 'min')-1)/len(all_debts)*100))
    net_worth_percentiles = dict(zip(all_net_worth,(stats.rankdata(all_net_worth, 'min')-1)/len(all_net_worth)*100))
    
    income_percentile = int(income_percentiles[user_profile.income/conversion])
    asset_percentile = int(asset_percentiles[user_profile.assets/conversion])
    debt_percentile = int(debt_percentiles[user_profile.debts/conversion])
    net_worth_percentile = int(net_worth_percentiles[user_profile.assets/conversion - user_profile.debts/conversion])

    suffixes = {0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th'}
    income_suffix = suffixes[income_percentile % 10]
    asset_suffix = suffixes[asset_percentile % 10]
    debt_suffix = suffixes[debt_percentile % 10]
    net_worth_suffix = suffixes[net_worth_percentile % 10]

    new_data = {"income_percentile": income_percentile, "asset_percentile": asset_percentile,
        "debt_percentile": debt_percentile, "net_worth_percentile": net_worth_percentile,
        "hide_message": hide_message, "income_suffix": income_suffix, "asset_suffix": asset_suffix,
        "debt_suffix": debt_suffix, "net_worth_suffix": net_worth_suffix, "no_of_users": no_of_users
        }
    
    return JsonResponse(new_data, status=201)

@csrf_exempt
@login_required
def filter_race(request):
    price()
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    selected_race = data['race']

    user_profile = Profile.objects.get(author=request.user)
    all_income = []
    all_assets = []
    all_debts = []
    hide_message = 0

    # determine if user selected 'All'
    if selected_race == 'AL':
        all_users = Profile.objects.all()
        hide_message = 1
        no_of_users = len(all_users)
    else:
        all_users = Profile.objects.filter(race=selected_race)
        if user_profile not in all_users:
            no_of_users = len(all_users) + 1
        else:
            no_of_users = len(all_users)
        
    for user in all_users:
        if user.author != request.user:
            conversion = Decimal(price_dictionary[user.currency])
            all_income.append(user.income/conversion)
            all_assets.append(user.assets/conversion)
            all_debts.append(user.debts/conversion)
    
    conversion = Decimal(price_dictionary[user_profile.currency])
    all_income.append(user_profile.income/conversion)
    all_assets.append(user_profile.assets/conversion)
    all_debts.append(user_profile.debts/conversion)

    all_net_worth = [all_assets[i] - all_debts[i] for i in range(len(all_debts))]

    all_income.sort()
    all_assets.sort()
    all_debts.sort()
    all_net_worth.sort()

    #from https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile
    income_percentiles = dict(zip(all_income,(stats.rankdata(all_income, 'min')-1)/len(all_income)*100))
    asset_percentiles = dict(zip(all_assets,(stats.rankdata(all_assets, 'min')-1)/len(all_assets)*100))
    debt_percentiles = dict(zip(all_debts,(stats.rankdata(all_debts, 'min')-1)/len(all_debts)*100))
    net_worth_percentiles = dict(zip(all_net_worth,(stats.rankdata(all_net_worth, 'min')-1)/len(all_net_worth)*100))
    
    income_percentile = int(income_percentiles[user_profile.income/conversion])
    asset_percentile = int(asset_percentiles[user_profile.assets/conversion])
    debt_percentile = int(debt_percentiles[user_profile.debts/conversion])
    net_worth_percentile = int(net_worth_percentiles[user_profile.assets/conversion - user_profile.debts/conversion])

    suffixes = {0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th'}
    income_suffix = suffixes[income_percentile % 10]
    asset_suffix = suffixes[asset_percentile % 10]
    debt_suffix = suffixes[debt_percentile % 10]
    net_worth_suffix = suffixes[net_worth_percentile % 10]

    new_data = {"income_percentile": income_percentile, "asset_percentile": asset_percentile,
        "debt_percentile": debt_percentile, "net_worth_percentile": net_worth_percentile,
        "hide_message": hide_message, "income_suffix": income_suffix, "asset_suffix": asset_suffix,
        "debt_suffix": debt_suffix, "net_worth_suffix": net_worth_suffix, "no_of_users": no_of_users
        }
    
    return JsonResponse(new_data, status=201)

@csrf_exempt
@login_required
def filter_ethnicity(request):
    price()
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    selected_ethnicity = data['ethnicity']

    user_profile = Profile.objects.get(author=request.user)
    all_income = []
    all_assets = []
    all_debts = []
    hide_message = 0

    # determine if user selected 'All'
    if selected_ethnicity == 'AL':
        all_users = Profile.objects.all()
        hide_message = 1
        no_of_users = len(all_users)
    else:
        all_users = Profile.objects.filter(ethnicity=selected_ethnicity)
        if user_profile not in all_users:
            no_of_users = len(all_users) + 1
        else:
            no_of_users = len(all_users)
        
    for user in all_users:
        if user.author != request.user:
            conversion = Decimal(price_dictionary[user.currency])
            all_income.append(user.income/conversion)
            all_assets.append(user.assets/conversion)
            all_debts.append(user.debts/conversion)
    
    conversion = Decimal(price_dictionary[user_profile.currency])
    all_income.append(user_profile.income/conversion)
    all_assets.append(user_profile.assets/conversion)
    all_debts.append(user_profile.debts/conversion)

    all_net_worth = [all_assets[i] - all_debts[i] for i in range(len(all_debts))]

    all_income.sort()
    all_assets.sort()
    all_debts.sort()
    all_net_worth.sort()

    # from https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile
    income_percentiles = dict(zip(all_income,(stats.rankdata(all_income, 'min')-1)/len(all_income)*100))
    asset_percentiles = dict(zip(all_assets,(stats.rankdata(all_assets, 'min')-1)/len(all_assets)*100))
    debt_percentiles = dict(zip(all_debts,(stats.rankdata(all_debts, 'min')-1)/len(all_debts)*100))
    net_worth_percentiles = dict(zip(all_net_worth,(stats.rankdata(all_net_worth, 'min')-1)/len(all_net_worth)*100))
    
    income_percentile = int(income_percentiles[user_profile.income/conversion])
    asset_percentile = int(asset_percentiles[user_profile.assets/conversion])
    debt_percentile = int(debt_percentiles[user_profile.debts/conversion])
    net_worth_percentile = int(net_worth_percentiles[user_profile.assets/conversion - user_profile.debts/conversion])

    # determine suffix
    suffixes = {0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th'}
    income_suffix = suffixes[income_percentile % 10]
    asset_suffix = suffixes[asset_percentile % 10]
    debt_suffix = suffixes[debt_percentile % 10]
    net_worth_suffix = suffixes[net_worth_percentile % 10]

    new_data = {"income_percentile": income_percentile, "asset_percentile": asset_percentile,
        "debt_percentile": debt_percentile, "net_worth_percentile": net_worth_percentile,
        "hide_message": hide_message, "income_suffix": income_suffix, "asset_suffix": asset_suffix,
        "debt_suffix": debt_suffix, "net_worth_suffix": net_worth_suffix, "no_of_users": no_of_users
        }
    
    return JsonResponse(new_data, status=201)

@csrf_exempt
@login_required
def filter_age(request):
    price()
    price_model = Price.objects.get(created='Y')
    price_dictionary = json.loads(price_model.response)['rates']
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    data = json.loads(request.body)

    selected_age = data['age_group']
    # print(type(selected_age))
    user_profile = Profile.objects.get(author=request.user)
    all_income = []
    all_assets = []
    all_debts = []
    hide_message = 0

    # determine if user selected 'All'
    if selected_age == '0':
        all_users = Profile.objects.all()
        hide_message = 1
        no_of_users = len(all_users)
    else:
        all_users = Profile.objects.filter(age_group=selected_age)
        if user_profile not in all_users:
            no_of_users = len(all_users) + 1
        else:
            no_of_users = len(all_users)
        
    for user in all_users:
        if user.author != request.user:
            conversion = Decimal(price_dictionary[user.currency])
            all_income.append(user.income/conversion)
            all_assets.append(user.assets/conversion)
            all_debts.append(user.debts/conversion)
    
    conversion = Decimal(price_dictionary[user_profile.currency])
    all_income.append(user_profile.income/conversion)
    all_assets.append(user_profile.assets/conversion)
    all_debts.append(user_profile.debts/conversion)

    all_net_worth = [all_assets[i] - all_debts[i] for i in range(len(all_debts))]

    all_income.sort()
    all_assets.sort()
    all_debts.sort()
    all_net_worth.sort()


    # from https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile
    income_percentiles = dict(zip(all_income,(stats.rankdata(all_income, 'min')-1)/len(all_income)*100))
    asset_percentiles = dict(zip(all_assets,(stats.rankdata(all_assets, 'min')-1)/len(all_assets)*100))
    debt_percentiles = dict(zip(all_debts,(stats.rankdata(all_debts, 'min')-1)/len(all_debts)*100))
    net_worth_percentiles = dict(zip(all_net_worth,(stats.rankdata(all_net_worth, 'min')-1)/len(all_net_worth)*100))
    
    income_percentile = int(income_percentiles[user_profile.income/conversion])
    asset_percentile = int(asset_percentiles[user_profile.assets/conversion])
    debt_percentile = int(debt_percentiles[user_profile.debts/conversion])
    net_worth_percentile = int(net_worth_percentiles[user_profile.assets/conversion - user_profile.debts/conversion])

    # determine suffix
    suffixes = {0: 'th', 1: 'st', 2: 'nd', 3: 'rd', 4: 'th', 5: 'th', 6: 'th', 7: 'th', 8: 'th', 9: 'th'}
    income_suffix = suffixes[income_percentile % 10]
    asset_suffix = suffixes[asset_percentile % 10]
    debt_suffix = suffixes[debt_percentile % 10]
    net_worth_suffix = suffixes[net_worth_percentile % 10]

    new_data = {"income_percentile": income_percentile, "asset_percentile": asset_percentile,
        "debt_percentile": debt_percentile, "net_worth_percentile": net_worth_percentile,
        "hide_message": hide_message, "income_suffix": income_suffix, "asset_suffix": asset_suffix,
        "debt_suffix": debt_suffix, "net_worth_suffix": net_worth_suffix, "no_of_users": no_of_users
        }
    
    return JsonResponse(new_data, status=201)