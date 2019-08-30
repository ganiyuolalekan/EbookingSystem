from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_category = models.CharField(max_length=50)
    movie_img = models.ImageField(upload_to='movies/static/images/')
    movie_ticket_number = models.IntegerField()
    movie_ticket_booked = models.IntegerField(default=0, blank=True)
    movie_ticket_price = models.FloatField()
    movie_venue = models.CharField(max_length=150)
    movie_show_date = models.DateTimeField()
    movie_description = models.TextField()

    objects = models.Manager()


    def __str__(self):
        return " ends ".join([str(self.movie_name), str(self.movie_show_date)])

# Model to handle all movies available on the site....
# Only to be adjusted if compulsory....


class Attendant(models.Model):
    attendant_name = models.CharField(max_length=35)
    attendant_booked_sit = models.IntegerField(blank=True)
    attendant_booked_movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.attendant_name

# Model to handle all attendant available for each movie....
# Only to be adjusted if compulsory....
