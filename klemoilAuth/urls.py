from klemoilAuth.views import Login
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
