from collected_items.models import CollectedItems
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView


# Create your views here.

class HomeView(LoginRequiredMixin ,View):
    def get(self, request):
        return render(request, 'home.html')


class CollectedList(ListView):
    model = CollectedItems
    template_name = 'collected items/collectedList.html'
