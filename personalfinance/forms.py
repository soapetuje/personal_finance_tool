from django import forms

ETHNICITY_CHOICES = [
        ('HI','Hispanic or Latino'),
        ('NH','Not Hispanic or Latino'),
        ('OT', 'Other')
    ]

ETHNICITY_FILTER = [('AL', 'All')] + ETHNICITY_CHOICES

RACE_CHOICES = [
    ('AI','American Indian or Alaska Native'),
    ('AS','Asian'),
    ('BL','Black or African American'),
    ('NH','Native Hawaiian or Other Pacific Islander'),
    ('WH', 'White'),
    ('OT', 'Other')
]

RACE_FILTER = [('AL', 'All')] + RACE_CHOICES

EDUCATION_CHOICES = [
    ('NH','No High School'),
    ('HS','High School Diploma or GED'),
    ('AS',"Associate's Degree"),
    ('BS',"Bachelor's Degree"),
    ('MS',"Master's Degree"),
    ('DC','Doctorate Degree'),
    ('PD','Professional Degree'),
    ('OT', 'Other')
]

EDUCATION_FILTER = [('AL', 'All')] + EDUCATION_CHOICES

ALL = 0
UNDER_10 = 10
UNDER_20 = 20
UNDER_30 = 30
UNDER_40 = 40
UNDER_50 = 50
UNDER_60 = 60
OVER_60 = 70

AGE_CHOICES = [
        (UNDER_10,'0 - 9'),
        (UNDER_20,'10 - 19'),
        (UNDER_30,'20 - 29'),
        (UNDER_40,'30 - 39'),
        (UNDER_50,'40 - 49'),
        (UNDER_60,'50 - 59'),
        (OVER_60,'60 And Over')
    ]

AGE_FILTER = [(ALL, 'All')] + AGE_CHOICES

# made call at http://api.exchangeratesapi.io/v1/symbols?access_key=API_KEY
#converted to usable format for model
symbols = {"AED":"United Arab Emirates Dirham","AFN":"Afghan Afghani","ALL":"Albanian Lek","AMD":"Armenian Dram","ANG":"Netherlands Antillean Guilder","AOA":"Angolan Kwanza","ARS":"Argentine Peso","AUD":"Australian Dollar","AWG":"Aruban Florin","AZN":"Azerbaijani Manat","BAM":"Bosnia-Herzegovina Convertible Mark","BBD":"Barbadian Dollar","BDT":"Bangladeshi Taka","BGN":"Bulgarian Lev","BHD":"Bahraini Dinar","BIF":"Burundian Franc","BMD":"Bermudan Dollar","BND":"Brunei Dollar","BOB":"Bolivian Boliviano","BRL":"Brazilian Real","BSD":"Bahamian Dollar","BTC":"Bitcoin","BTN":"Bhutanese Ngultrum","BWP":"Botswanan Pula","BYN":"New Belarusian Ruble","BYR":"Belarusian Ruble","BZD":"Belize Dollar","CAD":"Canadian Dollar","CDF":"Congolese Franc","CHF":"Swiss Franc","CLF":"Chilean Unit of Account (UF)","CLP":"Chilean Peso","CNY":"Chinese Yuan","COP":"Colombian Peso","CRC":"Costa Rican Col\u00f3n","CUC":"Cuban Convertible Peso","CUP":"Cuban Peso","CVE":"Cape Verdean Escudo","CZK":"Czech Republic Koruna","DJF":"Djiboutian Franc","DKK":"Danish Krone","DOP":"Dominican Peso","DZD":"Algerian Dinar","EGP":"Egyptian Pound","ERN":"Eritrean Nakfa","ETB":"Ethiopian Birr","EUR":"Euro","FJD":"Fijian Dollar","FKP":"Falkland Islands Pound","GBP":"British Pound Sterling","GEL":"Georgian Lari","GGP":"Guernsey Pound","GHS":"Ghanaian Cedi","GIP":"Gibraltar Pound","GMD":"Gambian Dalasi","GNF":"Guinean Franc","GTQ":"Guatemalan Quetzal","GYD":"Guyanaese Dollar","HKD":"Hong Kong Dollar","HNL":"Honduran Lempira","HRK":"Croatian Kuna","HTG":"Haitian Gourde","HUF":"Hungarian Forint","IDR":"Indonesian Rupiah","ILS":"Israeli New Sheqel","IMP":"Manx pound","INR":"Indian Rupee","IQD":"Iraqi Dinar","IRR":"Iranian Rial","ISK":"Icelandic Kr\u00f3na","JEP":"Jersey Pound","JMD":"Jamaican Dollar","JOD":"Jordanian Dinar","JPY":"Japanese Yen","KES":"Kenyan Shilling","KGS":"Kyrgystani Som","KHR":"Cambodian Riel","KMF":"Comorian Franc","KPW":"North Korean Won","KRW":"South Korean Won","KWD":"Kuwaiti Dinar","KYD":"Cayman Islands Dollar","KZT":"Kazakhstani Tenge","LAK":"Laotian Kip","LBP":"Lebanese Pound","LKR":"Sri Lankan Rupee","LRD":"Liberian Dollar","LSL":"Lesotho Loti","LTL":"Lithuanian Litas","LVL":"Latvian Lats","LYD":"Libyan Dinar","MAD":"Moroccan Dirham","MDL":"Moldovan Leu","MGA":"Malagasy Ariary","MKD":"Macedonian Denar","MMK":"Myanma Kyat","MNT":"Mongolian Tugrik","MOP":"Macanese Pataca","MRO":"Mauritanian Ouguiya","MUR":"Mauritian Rupee","MVR":"Maldivian Rufiyaa","MWK":"Malawian Kwacha","MXN":"Mexican Peso","MYR":"Malaysian Ringgit","MZN":"Mozambican Metical","NAD":"Namibian Dollar","NGN":"Nigerian Naira","NIO":"Nicaraguan C\u00f3rdoba","NOK":"Norwegian Krone","NPR":"Nepalese Rupee","NZD":"New Zealand Dollar","OMR":"Omani Rial","PAB":"Panamanian Balboa","PEN":"Peruvian Nuevo Sol","PGK":"Papua New Guinean Kina","PHP":"Philippine Peso","PKR":"Pakistani Rupee","PLN":"Polish Zloty","PYG":"Paraguayan Guarani","QAR":"Qatari Rial","RON":"Romanian Leu","RSD":"Serbian Dinar","RUB":"Russian Ruble","RWF":"Rwandan Franc","SAR":"Saudi Riyal","SBD":"Solomon Islands Dollar","SCR":"Seychellois Rupee","SDG":"Sudanese Pound","SEK":"Swedish Krona","SGD":"Singapore Dollar","SHP":"Saint Helena Pound","SLL":"Sierra Leonean Leone","SOS":"Somali Shilling","SRD":"Surinamese Dollar","STD":"S\u00e3o Tom\u00e9 and Pr\u00edncipe Dobra","SVC":"Salvadoran Col\u00f3n","SYP":"Syrian Pound","SZL":"Swazi Lilangeni","THB":"Thai Baht","TJS":"Tajikistani Somoni","TMT":"Turkmenistani Manat","TND":"Tunisian Dinar","TOP":"Tongan Pa\u02bbanga","TRY":"Turkish Lira","TTD":"Trinidad and Tobago Dollar","TWD":"New Taiwan Dollar","TZS":"Tanzanian Shilling","UAH":"Ukrainian Hryvnia","UGX":"Ugandan Shilling","USD":"United States Dollar","UYU":"Uruguayan Peso","UZS":"Uzbekistan Som","VEF":"Venezuelan Bol\u00edvar Fuerte","VND":"Vietnamese Dong","VUV":"Vanuatu Vatu","WST":"Samoan Tala","XAF":"CFA Franc BEAC","XAG":"Silver (troy ounce)","XAU":"Gold (troy ounce)","XCD":"East Caribbean Dollar","XDR":"Special Drawing Rights","XOF":"CFA Franc BCEAO","XPF":"CFP Franc","YER":"Yemeni Rial","ZAR":"South African Rand","ZMK":"Zambian Kwacha (pre-2013)","ZMW":"Zambian Kwacha","ZWL":"Zimbabwean Dollar"}
CURRENCY_CHOICES = []

for key in symbols:
    a = (key, symbols[key])
    CURRENCY_CHOICES.append(a)


class NewProfile(forms.Form):
    age_group = forms.ChoiceField(choices=AGE_CHOICES, required=True)
    education = forms.ChoiceField(choices= EDUCATION_CHOICES, required=True)
    ethnicity = forms.ChoiceField(choices= ETHNICITY_CHOICES, required=True)
    race = forms.ChoiceField(choices= RACE_CHOICES, required=True)
    currency = forms.ChoiceField(choices= CURRENCY_CHOICES, required=True, initial='EUR')
    income = forms.DecimalField(label="Income", max_digits=200, decimal_places=8, required=True, help_text='Yearly Income')
    assets = forms.DecimalField(label="Assets", max_digits=200, decimal_places=8, required=True, help_text='Total Value of All Assets')
    debts = forms.DecimalField(label="Debts", max_digits=200, decimal_places=8, required=True, help_text='Total Value of All Debts')

class Filter(forms.Form):
    currency = forms.ChoiceField(choices= CURRENCY_CHOICES, required=True, initial='EUR')
    age_group = forms.ChoiceField(choices=AGE_FILTER, required=True)
    education = forms.ChoiceField(choices= EDUCATION_FILTER, required=True, initial='AL')
    ethnicity = forms.ChoiceField(choices= ETHNICITY_FILTER, required=True, initial='AL')
    race = forms.ChoiceField(choices= RACE_FILTER, required=True, initial='AL')
    
class Base_Currency(forms.Form):
    base_currency = forms.ChoiceField(choices= CURRENCY_CHOICES, required=True, initial='EUR')
    
