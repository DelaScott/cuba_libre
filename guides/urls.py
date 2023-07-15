from django.urls import path
from . import views

app_name = 'guides'

urlpatterns = [
    path('', views.guide_list, name='guide_list'),
    path('guide/<int:pk>/', views.guide_detail, name='guide_detail'),
    # Добавьте другие URL-шаблоны для ваших представлений
]
