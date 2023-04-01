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


class ArticleCreateView(CreateView):
    model = Article
    fields = '__all__'
    success_url = '/article/'


class ArticleUpdateView(UpdateView):
    model = Article
    fields = '__all__'
    success_url = '/article/'


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = '/article/'
