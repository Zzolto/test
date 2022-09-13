from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from django.urls import reverse
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200,verbose_name='Название')
    shortDescription = models.TextField(blank=True, verbose_name='Краткое описание')
    fullDescription = models.TextField(blank=True, verbose_name='Описание')
    newsType = models.ForeignKey('Type', on_delete= models.PROTECT, verbose_name='Тип')


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural='Новости'

class Type(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Тип новости', blank=True)
    color = models.CharField(max_length=20, db_index= True, verbose_name='Цвет')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type',kwargs={'type_id': self.pk})

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural='Типы новостей'
        ordering = ['title']