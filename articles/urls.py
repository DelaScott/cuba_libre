from django.urls import path
from .views import articles_list, article_detail

app_name = 'articles'

urlpatterns = [
    path('articles/', articles_list, name='articles_list'),
    path('articles/<int:pk>/', article_detail, name='article_detail'),
]
