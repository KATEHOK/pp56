from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Person(User):
    class Meta:
        proxy = True
        ordering = ['id']

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_id': self.id})


class Species(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Название вида')
    title_plural = models.CharField(max_length=30, unique=True, verbose_name='Название вида (мн. ч.)', null=True)
    slug = models.SlugField(max_length=30, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Биологический вид'
        verbose_name_plural = 'Биологические виды'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('species', kwargs={'species_slug': self.slug})


class Pet(models.Model):
    name = models.CharField(max_length=30, verbose_name='Кличка')
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='main/img/pet/%Y/%m/%d', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_edit = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    owner = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name='Хозяин')
    species = models.ForeignKey('Species', on_delete=models.PROTECT, verbose_name='Биологический вид')

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pet', kwargs={'pet_slug': self.slug})

    def get_edit_url(self):
        return reverse('pet_edit', kwargs={'pet_slug': self.slug})

    def get_delete_url(self):
        return reverse('pet_delete', kwargs={'pet_slug': self.slug})

    def get_owner(self):
        return Person.objects.get(id=self.owner_id)