from .forms import Tickets
from django.db.models import Q
from .models import Movie, Attendant
from django.shortcuts import render, redirect, reverse


def index(request):
    categories = ()
    for movie in Movie.objects.all():
        category = movie.movie_category
        if category not in categories: categories += category,
    # Get all movies category in the database....

    name = []
    sub_book = []
    for category in categories:
        categorical_movies = list(Movie.objects.filter(movie_category=category))
        name.append(category)
        if len(categorical_movies) > 4:
            sub_book.append(categorical_movies[:4])
        else:
            sub_book.append(categorical_movies)
    # Arranges all name category_movie_name to movies_set

    movies = zip(name, sub_book)
    # Creates a zip categorization of all category_movie_name to movies_set

    return render(request, 'movies/movie_template/index.html', {'movies': movies})

# This handles all the books displayed at the index page


def category(request, category_name):
    movies = Movie.objects.filter(movie_category=category_name)

    return render(request, 'movies/movie_template/category.html', {
        'category_name': category_name,
        'movies': movies,
    })

# This handles all the books displayed at the category page


def movie_name(request, movie_name):
    movie = Movie.objects.get(movie_name=movie_name)

    return render(request, 'movies/movie_template/movie_detail.html', {'movie': movie})

# This handles all the books displayed at the book detail page


def tickets(request, movie_name):
    movie = Movie.objects.get(movie_name=movie_name)
    if request.method == 'POST':
        form = Tickets(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name, num_of_site = cd['name'], cd['num_of_sits']
            Attendant.objects.create(
                attendant_name=name,
                attendant_booked_sit=num_of_site,
                attendant_booked_movie=movie
            )
            return redirect(reverse('payment:process', args=[
                movie_name,
                num_of_site,
                name,
            ]))
            # Ensure to fix payment gateway link....
            # Performs the necessary calculations to aid with ticket handling....
    else:
        return render(request, 'movies/movie_template/ticket_form.html', {
            'forms': Tickets(),
            'movie': movie,
        })

# Handles all processes for ticket booking and attendant management.....


def search(request):
    query = request.GET.get('q')
    result = Movie.objects.filter(Q(movie_name__icontains=query) | Q(movie_category__icontains=query))
    return render(request, 'movies/movie_template/category.html', {
        'category_name': 'Search result on "' + query + '"',
        'movies': result,
    })

# Handles the search query
