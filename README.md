# Personal Finance Tool

With the increasing interest in personal finance and financial independence, this website is intended as a tool to help the user understand where they rank relative to other users on the platform and ultimately help them achieve Financial Independence as they work to improve their ranking.

## How to Run
* Go to [Exchange Rate API](https://exchangeratesapi.io/) and register to get an API KEY
* Set Key as an environment variable called 'EXCHANGE_RATE_KEY' (or change lines 19 and 21 in ['views.py'](personalfinance/views.py))
* pip install the requirements file
* Go to your terminal
* Change your directory to the same folder as the ['manage.py'](personalfinance/views.py) file
* Run 'python manage.py runserver'
* Click on development server link

## How it works
### Getting Set Up
This page is built using the [Django Web Framework](https://www.djangoproject.com/) along with HTML, JavaScript and [Bootstrap](https://getbootstrap.com/) for styling

After registering an account users are prompted for the following information:
*Age Group
*Education Level
*Race and Ethnicity
*Preferred Currency
*Yearly Income
*Total Value of All Assets
*Total Value of All Debts
This information is used later in the dashboard to show where the user falls relative to other users in the 
selected filter.

You can watch a video demo [here](https://www.youtube.com/watch?v=B2NrrC0r4ps&t=55s)

### Exchange Rates
Exchange rate data is queried daily from the [Exchange Rate API](https://exchangeratesapi.io/).
This is then used to bring all users to a base currency (Euro) in order to correctly calculate the percentiles
Current exchange rates are also displayed in a separate page

### Dash Board
On the dashboard, the user gets access to four cards which shows, Income, Assets, Debts and Net worth along with their percentile for all users on the platform (default filter)

There are filters which do different things

The *Currency* filter allows the user to convert between the currencies available

The *Age, Ethnicity, Education and Race* filters allows the user to determine their percentile for specific subsets within those groups. 

## Implementation

The website's files consists of:
* ['styles.css'](personalfiance/static/personalfinance/styles.css)
* ['update_currency.js'](personalfiance/static/personalfinance/update_currency.js)
* ['update_filters.js'](personalfiance/static/personalfinance/update_filters.js)
* ['dashboard.html'](personalfinance/templates/personalfinance/dashboard.html)
* ['first_profile.html'](personalfinance/templates/personalfinance/first_profile.html)
* ['index.html'](personalfinance/templates/personalfinance/index.html)
* ['layout.html'](personalfinance/templates/personalfinance/layout.html)
* ['login.html'](personalfinance/templates/personalfinance/login.html)
* ['profile.html'](personalfinance/templates/personalfinance/profile.html)
* ['rates.html'](personalfinance/templates/personalfinance/rates.html)
* ['register.html'](personalfinance/templates/personalfinance/register.html)
* ['forms.py'](personalfinance/forms.py)
* ['models.py'](personalfinance/models.py)
* ['urls.py'](personalfinance/urls.py)
* ['views.py'](personalfinance/views.py)

### ['styles.css'](personalfiance/static/personalfinance/styles.css)

This file contains styling choices that were used to overwrite some default bootstrap behaviors.
Also implemented the background color change using the :hover selector which served as an indicator to the user if their net worth was negative and hopefully motivate them to take action to improve it.

### ['update_currency.js'](personalfiance/static/personalfinance/update_currency.js)

This file is used in ['profile.html'](personalfinance/templates/personalfinance/profile.html) to update the users amounts when the currency dropdown is changed. This is achieved using an event listener as well as an asynchronous request to convert the amounts to the specified currency.

### ['update_filters.js'](personalfiance/static/personalfinance/update_filters.js)

This file is used in ['dashboard.html'](personalfinance/templates/personalfinance/dashboard.html) for the client side filtering and currency updates. This file also handles updating the background color shown on hover if the amount in the net worth card is negative

### ['dashboard.html'](personalfinance/templates/personalfinance/dashboard.html)

This django template renders the dashboard for the user. It contains the 5 filters the user can use to update currency or percentile scores as well as the 4 cards displaying the financial metrics

### ['first_profile.html'](personalfinance/templates/personalfinance/first_profile.html)

This template shows a user profile when a user registers. The reason for having a separate template was to exclude the Javascript which was used to update currency as that didn't make sense as a feature when the user is setting up their profile for the first time.

### ['index.html'](personalfinance/templates/personalfinance/index.html)

This template displays information about the website. It is used as the landing page. I chose to make this page because I needed a page for new users who hadn't registered and it also served as an 'About' page

### ['layout.html'](personalfinance/templates/personalfinance/layout.html)

This template is used as a blueprint from which all other pages are based

### ['login.html'](personalfinance/templates/personalfinance/login.html)

This template is used to collect and send user credentials for validation and logging into the platform

### ['profile.html'](personalfinance/templates/personalfinance/profile.html)

This template simply displays a form which contains all the user's information which can be edited and resubmitted

### ['rates.html'](personalfinance/templates/personalfinance/rates.html)

This template is used to display the exchange rates in a tabular form with a drop down to select the base currency

### ['register.html'](personalfinance/templates/personalfinance/register.html)

This template is used to display a form which collects username, first name, last name, email, password and password confirmation in order to register and log in the user

### ['forms.py'](personalfinance/forms.py)

This file contains 3 forms that are used through out the website. They include:

* New Profile: This contains user demographic information in addition to assets, debts and income
* Filter: This contains choice fields for all the filters (currency, education, ethinicity, race, age group)
* Base Currency: This contains a choice field for the currency

### ['models.py'](personalfinance/models.py)

This file contains 3 models that are used to access and mangage data. They include:

* User Model: This inherits from the AbstractUser django class
* Profile Model: This is used to manange user demographic and financial information
* Price Model: This is used to store the data from the Exchange Rate API which allowed me to query daily and stay in the free tier

### ['urls.py'](personalfinance/urls.py)

This file contains all the various routes that a user can visit on the website as well as the views for each route.
There are 12 routes in total and 5 are for the asynchronous JavaScript requests

### ['views.py'](personalfinance/views.py)

This file is the main component of the back-end of the website. It contains all the views which handles the logic of the website before rendering the page that the user sees. It also contains the function which queries the Exchange Rate Api in order to update the Price Model.
The percentiles were calculated using a post from [stackoverflow](https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile) as a guide

The views are as follows:
* index: Renders the landing page (index.html)
* rates: Displays or updates the exchange rates page (rates.html)
* dashboard: Displays the dashboard
* login_view: Handles user authentication and either redirects the user to the landing page (index.html) or back to the login page (login.html)
* logout_view: Logs the user out and redirects them to the landing page (index.html)
* register: Creates a new user, signs in the user and redirects them to the landing page (index.html)
* profile: Displays or updates the user profile information
* update_currency: Queries Price model for exchange rate data and converts the numbers supplied in the request and returns a JSON response with the converted numbers
* filter_education: Queries Profile model with the selected education filter, converts all users back to the Euro, calculates the percentiles for all users, selects the current user's percentile for all metrics (assets, income, debts, liabilites), determines what suffix to use i.e 'st', 'nd', 'rd', 'th'. Finally returns a JSON response back.
* filter_ethnicity: Queries Profile model with the selected ethnicity filter, converts all users back to the Euro, calculates the percentiles for all users, selects the current user's percentile for all metrics (assets, income, debts, liabilites), determines what suffix to use i.e 'st', 'nd', 'rd', 'th'. Finally returns a JSON response back.
* filter_race: Queries Profile model with the selected race filter, converts all users back to the Euro, calculates the percentiles for all users, selects the current user's percentile for all metrics (assets, income, debts, liabilites), determines what suffix to use i.e 'st', 'nd', 'rd', 'th'. Finally returns a JSON response back.
* filter_age: Queries Profile model with the selected age group filter, converts all users back to the Euro, calculates the percentiles for all users, selects the current user's percentile for all metrics (assets, income, debts, liabilites), determines what suffix to use i.e 'st', 'nd', 'rd', 'th'. Finally returns a JSON response back.

## Distinctiveness and Complexity
I believe this project meets the distinctiveness and complexity criteria as it is not the same as any of the projects I did for this course. I borrowed elements from lectures (mainly how to get forex data) but the idea and execution of the project are my own. The amount of bookmarks I have in my browser related to this project shows that it wasn't a walk in the park. From communicating with the API (the method from the lecture wasn't enough for my application), [making Django form fields pretty with bootstrap](https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html), [handling choices the right way](https://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/), [percentiles](https://stackoverflow.com/questions/12414043/map-each-list-value-to-its-corresponding-percentile), [reading the JSON docs](https://docs.python.org/3/library/json.html) and watching the CS50 lectures and other YouTube web development lectures when I got stuck, I was able to learn a lot while implementing ths project.
Also, this project utilizes HTML, CSS, Git, Python, Django, JavaScript and Security principles as a way to tie it back to the lectures.
Looking back, if I had a better planned project, I would have been able to implement automated testing as opposed to the manual testing I did for the project.

## Reflection
This project was extremely frustrating to complete; there were a lot of times I just wanted to quit and give up. I actually stopped working on it for a couple of months and I learned a valuable lesson in keeping proper documentation as I basically had to start again from scratch because I couldn't follow what I had previously done. On my second go, I removed features (the filter feature for example) and broke it into simpler parts. As I was able to complete those parts, I was slowly able to bring features back until I had something I was proud of.

## Limitations

One limitation is that only one group can be used as a filter at a time

## Further Improvement

Figuring out how to host this on a live website