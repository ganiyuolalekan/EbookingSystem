from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('movie/<str:movie_name>/', views.movie_name, name='movie_name'),
    path('ticket/<str:movie_name>/', views.tickets, name='tickets'),
]
