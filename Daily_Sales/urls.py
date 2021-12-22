from django.urls import path
from .views import HomeView, Sales, SalesCreate, SalesDelete, SalesDetail, SalesEdit
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('salesList', Sales.as_view(), name='salesList'),
    path('salesUpdate/<int:pk>/', SalesEdit.as_view(), name='salesUpdate'),
    path('salesDelete/<int:pk>/', SalesDelete.as_view(), name='salesDelete'),
    # path('salesDetails/<int:pk>/', SalesDetail.as_view(), name='salesDetails'),
    path('addsales', SalesCreate.as_view(), name='addsales'),
    path('filtersales', views.filterSearch, name='filtersales'),
]
