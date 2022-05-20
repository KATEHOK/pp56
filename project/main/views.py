from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from .models import *
from .forms import *
from .utils import *


class ShowPet(MyLoginRequiredMixin, DataMixin, DetailView):
    model = Pet
    template_name = 'main/pet.html'
    slug_url_kwarg = 'pet_slug'
    context_object_name = 'pet'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['pet'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPet(MyLoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPetForm
    template_name = 'main/pet_add.html'
    success_url = reverse_lazy('index') # перенаправление после успеха

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление питомца')
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')

def index(request):
    menu = [
        {'title': 'TinderMeow', 'url_name': 'index'},
    ]
    return render(request, 'main/index.html', {'title': 'Главная', 'menu': menu})
