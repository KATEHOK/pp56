from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse
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
        c_def = self.get_user_context(title=context['pet'], id_selected=0, auth=True)
        return dict(list(context.items()) + list(c_def.items()))


class AddPet(MyLoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPetForm
    template_name = 'main/pet_add.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление питомца',
                                      id_selected=0, auth=True, user_id=self.request.user.id)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация', id_selected=0)
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
        c_def = self.get_user_context(title='Авторизация', id_selected=0)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')

def pet_edit(request, pet_slug):
    if not request.user.is_authenticated:
        redirect('login')
    pet = Pet.objects.get(slug=pet_slug)
    if not pet.owner_id == request.user.id:
        return redirect('index')
    return HttpResponse('edit')

def pet_delete(request, pet_slug):
    if not request.user.is_authenticated:
        redirect('login')
    pet = Pet.objects.get(slug=pet_slug)
    if not pet.owner_id == request.user.id:
        return redirect('index')
    return HttpResponse('delete')

def show_species(request, species_slug):
    if not request.user.is_authenticated:
        redirect('login')
    menu = [
        {'title': 'TinderMeow', 'url_name': 'index'},
        {'title': 'Добавление питомца', 'url_name': 'pet_add'},
    ]
    species = Species.objects.all()
    sp_selected = species.get(slug=species_slug)
    pets = Pet.objects.filter(species_id=sp_selected.id)
    context = {
        'title': sp_selected.title_plural,
        'menu': menu,
        'pets': pets,
        'species': species,
        'id_selected': sp_selected.id,
    }
    return render(request, 'main/layout.html', context=context)

def show_all(request):
    if not request.user.is_authenticated:
        redirect('login')
    menu = [
        {'title': 'TinderMeow', 'url_name': 'index'},
        {'title': 'Добавление питомца', 'url_name': 'pet_add'},
    ]
    pets = Pet.objects.all()
    species = Species.objects.all()
    context = {
        'title': 'Все питомцы',
        'menu': menu,
        'pets': pets,
        'species': species,
        'id_selected': -1,
    }
    return render(request, 'main/layout.html', context=context)

def show_user(request, user_id):
    if not request.user.is_authenticated:
        redirect('login')
    if user_id == request.user.id:
        return redirect('index')
    menu = [
        {'title': 'TinderMeow', 'url_name': 'index'},
        {'title': 'Добавление питомца', 'url_name': 'pet_add'},
    ]
    pets = Pet.objects.filter(owner_id=user_id)
    if len(pets) == 0:
        raise Http404()
    species = Species.objects.all()
    username = (Person.objects.get(id=user_id)).username
    context = {
        'title': f'Питомцы {username}',
        'menu': menu,
        'pets': pets,
        'species': species,
        'id_selected': 0,
    }
    return render(request, 'main/layout.html', context=context)

def index(request):
    if not request.user.is_authenticated:
        redirect('login')
    menu = [
        {'title': 'TinderMeow', 'url_name': 'index'},
        {'title': 'Добавление питомца', 'url_name': 'pet_add'},
    ]
    pets = Pet.objects.filter(owner_id=request.user.id)
    species = Species.objects.all()
    context = {
        'title': 'Мои питомцы',
        'menu': menu,
        'pets': pets,
        'species': species,
        'id_selected': 0,
    }
    return render(request, 'main/layout.html', context=context)

