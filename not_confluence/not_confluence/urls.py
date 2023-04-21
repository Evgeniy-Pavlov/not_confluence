"""not_confluence URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp.views import ProjectListView, ArticleListView, ArticleDetailView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView, ProjectCreateView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('article/', ArticleListView.as_view()),
    path('project-list/', ProjectListView.as_view()),
    path('article-detail/<int:pk>/', ArticleDetailView.as_view()),
    path('article-create/', ArticleCreateView.as_view()),
    path('article-update/<int:pk>/', ArticleUpdateView.as_view()),
    path('article-delete/<int:pk>/', ArticleDeleteView.as_view()),
    path('project-create/', ProjectCreateView.as_view()),
    path('project-detail/<int:pk>/', ProjectDetailView.as_view()),
    path('project-update/<int:pk>/', ProjectUpdateView.as_view()),
    path('project-delete/<int:pk>/', ProjectDeleteView.as_view())

]
