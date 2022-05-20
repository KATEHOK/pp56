from django.contrib import admin

from .models import *

class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time_add', 'time_edit', 'photo', 'is_published']
    list_display_links = ['id', 'name']
    search_fields = ('title', 'description')
    list_editable = ['is_published']
    list_filter = ['is_published', 'time_add', 'time_edit']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Pet, PetAdmin)