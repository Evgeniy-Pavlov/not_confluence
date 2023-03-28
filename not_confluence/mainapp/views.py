from django.shortcuts import render
from .models import User, Article, Project
from django.views.generic import ListView

# Create your views here.

def article_view(request):
    article = Article.objects.all()
    return render(request, 'mainapp/article.html', {'article': article})


class ProjectListView(ListView):
    model = Project