from django.urls import path

from . import views

# app_name = 'personalfinance'
urlpatterns = [
    path("", views.index, name = "index"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("rates", views.rates, name="rates"),

    #API Routes
    path("update", views.update_currency, name="update"),
    path("filter_education", views.filter_education, name="filter_education"),
    path("filter_race", views.filter_race, name="filter_race"),
    path("filter_ethnicity", views.filter_ethnicity, name="filter_ethnicity"),
    path("filter_age", views.filter_age, name="filter_age"),
]