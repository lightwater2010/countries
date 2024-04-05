from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from all_countries.forms import *
from requests import *
from all_countries.models import Countries

from all_countries.utils import DataMixin


# Create your views here.
class HomePage(DataMixin,CreateView):
    form_class = Form_countries
    template_name = 'all_countries/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Главная страница')
        return dict( list(context.items()) + list(context2.items()) )
class Search(LoginRequiredMixin,DataMixin,DetailView):
    model = Countries
    template_name = 'all_countries/home.html'
    context_object_name = 'c'
    slug_url_kwarg = 'search'
    login_url = 'login'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context2 = self.get_user_context(title='Найденная страна',search=self.request.GET.get('search'))
        return dict(list(context.items()) + list(context2.items()))

    def get_object(self):
        model_ = Countries.objects.all().delete()
        

        country = self.request.GET.get('search')

        try:
            request = get(f'https://restcountries.com/v3.1/name/{country}?fullText=true').json()
            name = request[0].get('name').get('official')
            currincies = request[0].get('currencies')
            capital = request[0].get('capital')
            region = request[0].get('subregion')
            language = request[0].get('languages')
            true_language = ','.join(list(language.values()))
            true_currincies = f"{list(currincies.values())[0]['name']} {list(currincies.values())[0]['symbol']}"
            name_in_their_language = ','.join(request[0].get('altSpellings'))
            google_maps = request[0].get('maps')['googleMaps']
            flag = request[0].get('flags')['png']
            db = Countries()
            db.name = name
            db.currincies = true_currincies
            db.capital = capital[0]
            db.region = region
            db.language = true_language
            db.all_names = name_in_their_language
            db.google_maps = google_maps
            db.flag = flag
            db.save()
            return Countries.objects.order_by('-id')[0]
        except:
            ...


class RegisterPage(CreateView):
    form_class = RegistrationForm
    template_name = 'all_countries/registration.html'
    success_url = reverse_lazy('login')
    extra_context = {'title':'Регистрация'}

class Log_inPage(LoginView):
    form_class = Log_in
    template_name = 'all_countries/login.html'
    extra_context = {'title':'Авторизация'}
    def get_success_url(self):
        return reverse_lazy('home')
def logout_user(request):
    logout(request)
    return redirect('login')
def pagenotfound(request,exception):
    return HttpResponseNotFound('<img style="position: relative; left: 250px;" src="https://www.fiatprofessional.com/content/dam/moc/common/404-error/mobile/mobile_404.png" width=70% height=100%>')