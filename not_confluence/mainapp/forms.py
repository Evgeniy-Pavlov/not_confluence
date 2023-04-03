from django import forms
from .models import Article, Project

class ArticleForm(forms.ModelForm):

    title = forms.CharField(label='Заголовок')
    body = forms.CharField(label='Тело')

    class Meta:
        model = Article
        fields = ('title', 'body', 'author', 'project')


class ProjectForm(forms.ModelForm):

    name = forms.CharField(label='Имя проекта')

    class Meta:
        model = Project
        fields = ('name', 'user_create')