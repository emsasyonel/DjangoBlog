from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "article"

urlpatterns = [
    path('dashboard/',views.dashboard,name = "dashboard"),
    path("addarticle/",views.addarticle,name = "addarticle"),
    path("article/<int:id>",views.detail,name = "detail"),
    path("update/<int:id>",views.updateArticle,name = "update"),
    path("delete/<int:id>",views.delete,name = "delete"),
    path("",views.articles,name = "articles"),
    
]