from django.urls import reverse_lazy

from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

menu = [
    {'title': 'TinderMeow', 'url_name': 'index'},
]
authed = [
    {'title': 'TinderMeow', 'url_name': 'index'},
    {'title': 'Добавление питомца', 'url_name': 'pet_add'},
]

class DataMixin:
    menu = menu
    def get_user_context(self, **kwargs):
        context = kwargs
        if 'auth' in context:
            context['menu'] = authed
        else:
            context['menu'] = menu
        context['species'] = Species.objects.all()
        return context

class MyLoginRequiredMixin(LoginRequiredMixin):
    raise_exception = True
