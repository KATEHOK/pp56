from django.urls import reverse_lazy

from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

menu = [
    {'title': 'TinderMeow', 'url_name': 'index'},
]

class DataMixin:
    menu = menu
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

class MyLoginRequiredMixin(LoginRequiredMixin):
    raise_exception = True
