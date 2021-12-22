from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
