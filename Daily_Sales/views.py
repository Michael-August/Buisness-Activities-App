from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from Daily_Sales.models import Daily_Sales, Items
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(LoginRequiredMixin ,View):
    def get(self, request):
        return render(request, 'home.html')
    # model = Daily_Sales
    # template_name = 'home.html'


class Sales(LoginRequiredMixin ,ListView):
    model = Daily_Sales
    items = Items
    template_name = 'sales.html'
    context_object_name = 'sales'
    ordering = ['-date_purchased']


class SalesCreate(LoginRequiredMixin ,CreateView):
    model = Daily_Sales
    template_name = 'daily_sales_form.html'
    fields = ['customer_name', 'quantity', 'rate',  'payment_method','have_paid']
    success_url = reverse_lazy('salesList')


class SalesDetail(LoginRequiredMixin ,DetailView):
    model = Daily_Sales
    template_name = 'details.html'
    context_object_name = 'sales'


class SalesEdit(LoginRequiredMixin ,UpdateView):
    model = Daily_Sales
    template_name = 'daily_sales_form.html'
    fields = ['customer_name', 'item_purchased', 'quantity', 'rate',  'payment_method','have_paid']
    success_url = reverse_lazy('salesList')


class SalesDelete(LoginRequiredMixin ,DeleteView):
    model = Daily_Sales
    template_name = 'deleteConfirm.html'
    context_object_name = 'sales'
    success_url = reverse_lazy('salesList')


# A function that handles the if statement before I query the data base
def is_valid_queryparam(param):
    return param != '' and param is not None


def filterSearch(request):
    sales = Daily_Sales.objects.all()
    items = Items.objects.all()
    customer = request.GET.get('customer_name')
    item = request.GET.get('item_sold')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    debtors = request.GET.get('debtors')

    if is_valid_queryparam(customer):
        sales = sales.filter(customer_name__iexact=customer)

    elif is_valid_queryparam(item) and item != 'choose...':
        sales = sales.filter(item_purchased__icontains=item)

    if is_valid_queryparam(date_min):
        sales = sales.filter(date_purchased__gte=date_min)

    if is_valid_queryparam(date_max):
        sales = sales.filter(date_purchased__lt=date_max)

    if debtors == 'on':
        sales = sales.filter(have_paid=False)

    context = {
        'sales': sales,
        'items': items
    }
    return render(request, 'search.html', context)
