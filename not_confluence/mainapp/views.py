from django.shortcuts import render
from .models import User, Article, Project
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ArticleForm, ProjectForm

# Create your views here.

class ArticleListView(ListView):
    model = Article


class ProjectListView(ListView):
    model = Project


class ArticleDetailView(DetailView):
    model = Article


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/article/'


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = '/article/'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/article/'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = '/project-list/'

