from django.shortcuts import render
from .models import User, Article, Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def article_view(request):
    article = Article.objects.all()
    return render(request, 'mainapp/article_list.html', {'article': article})

class ArticleListView(ListView):
    model = Article


class ProjectListView(ListView):
    model = Project

