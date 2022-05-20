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
    path('pet/<slug:pet_slug>', ShowPet.as_view(), name='pet')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)