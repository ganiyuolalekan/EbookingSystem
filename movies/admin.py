from django.contrib import admin
from .models import Movie, Attendant

class MoviesAdmin(admin.ModelAdmin):
    list_display = 'movie_name', 'movie_category', 'movie_venue', 'movie_show_date'
    list_filter = 'movie_category',
    search_fields = 'movie_name',

class AttendantAdmin(admin.ModelAdmin):
    list_display = 'attendant_name', 'attendant_booked_sit', 'attendant_booked_movie'
    list_filter = 'attendant_booked_movie',
    search_fields = 'attendant_name',

admin.site.register(Movie, MoviesAdmin)
admin.site.register(Attendant, AttendantAdmin)

# Provides an handle to create, delete, alter and view all the movies and attendants in the database
