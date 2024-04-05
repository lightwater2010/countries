
from django.urls import path

from all_countries.views import *

from . import views


urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('search/',views.Search.as_view(),name='search'),
    path('register/',views.RegisterPage.as_view(),name='register'),
    path('login/',views.Log_inPage.as_view(),name='login'),
    path('logout/',views.logout_user,name='logout')


]

