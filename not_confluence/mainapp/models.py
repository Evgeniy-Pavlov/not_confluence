"""Тут хранятся классы таблиц."""
from datetime import datetime
from django.db import models


# Create your models here.

class User(models.Model):
    """Класс модели для описания сущностей пользователей."""
    login = models.CharField(unique=True, max_length=10)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    date_create = models.DateTimeField(null=True, default=datetime.now)


class Project(models.Model):
    """Класс модели для описания сущностей проектов."""
    name = models.CharField(unique=True, max_length=20)
    user_create = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_create = models.DateTimeField(null=True, default=datetime.now)
    user_update = models.ForeignKey(User, on_delete=models.SET_NULL,
                        blank=True, null=True, related_name='user_projects')
    date_update = models.DateTimeField(null=True, blank=True)


class Article(models.Model):
    """Класс модели для хранения статей."""
    title = models.CharField(unique=True, max_length=100)
    body = models.TextField(blank=True, null=True, max_length=10000)
    date_create = models.DateTimeField(null=True, default=datetime.now)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_update = models.ForeignKey(User, on_delete=models.SET_NULL,
                        blank=True, null=True, related_name='user_articles')
    date_update = models.DateTimeField(null=True, blank=True)
