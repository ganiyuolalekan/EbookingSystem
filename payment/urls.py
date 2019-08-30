from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('process/<str:movie_name>/<int:ticket_num>/<str:attendant_name>', views.payment_process, name='process'),
    path('done/<str:movie_name>/<int:ticket_num>/<str:attendant_name>', views.payment_done, name='done'),
    path('canceled/', views.payment_canceled, name='canceled'),
]