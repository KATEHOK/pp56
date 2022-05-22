from django.contrib import admin

from .models import *


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'title_plural', 'slug']
    list_display_links = ['title']
    search_fields = ('title', 'id')
    list_editable = ['id']
    prepopulated_fields = {'slug': ('title',)}


class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'species', 'owner', 'time_add', 'time_edit', 'is_published', 'photo']
    list_display_links = ['name']
    search_fields = ('name', 'description', 'id')
    list_editable = ['is_published']
    list_filter = ['is_published', 'time_add', 'time_edit']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Species, SpeciesAdmin)
admin.site.register(Pet, PetAdmin)