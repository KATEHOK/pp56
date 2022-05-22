from django.conf.urls.static import static
from django.urls import path

from project import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('pet_add', AddPet.as_view(), name='pet_add'),
    path('pet/<slug:pet_slug>', ShowPet.as_view(), name='pet'),
    path('species_all', show_all, name='all'),
    path('species/<slug:species_slug>', show_species, name='species'),
    path('user/<int:user_id>', show_user, name='user'),
    path('pet_edit/<slug:pet_slug>', pet_edit, name='pet_edit'),
    path('pet_delete/<slug:pet_slug>', pet_delete, name='pet_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)