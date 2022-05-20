from django.db import models
from django.urls import reverse


class Pet(models.Model):
    name = models.CharField(max_length=30, verbose_name='Кличка')
    slug = models.SlugField(max_length=60, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='main/img/pet/%Y/%m/%d', verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    time_edit = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pet', kwargs={'pet_slug':self.slug})

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'
        ordering = ['id']
