from django.shortcuts import render
from .models import User, Article, Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class ArticleListView(ListView):
    model = Article


class ProjectListView(ListView):
    model = Project


class ArticleDetailView(DetailView):
    model = Article
