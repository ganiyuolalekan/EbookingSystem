from django.conf import settings
from django.template.loader import get_template
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, reverse, HttpResponse
from .utils import render_to_pdf

from movies.models import Movie, Attendant
# This works properly...


@csrf_exempt
def payment_done(request, movie_name='Fatal Justice', ticket_num=2, attendant_name='lexzy'):
    movie = Movie.objects.get(movie_name=movie_name)
    movie.movie_ticket_number -= ticket_num
    movie.movie_ticket_booked += ticket_num
    movie.save()
    template = get_template('payment/done.html')
    context = {
        'attendant_name': attendant_name,
        'number_of_sits': ticket_num,
        'movie_name': movie_name,
        'movie_category': movie.movie_category,
    }
    html = template.render(context)
    pdf = render_to_pdf('payment/done.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % "12341231",
        content = "inline; filename='%s'" % filename,
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % filename,
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

# Made for complete payment and registers all payments


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')

# Made for invalid payment


def payment_process(request, movie_name=None, ticket_num=None, attendant_name=None, movie_category=None):
    movie = Movie.objects.get(movie_name=movie_name)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': movie.movie_ticket_price * ticket_num,
        'item_name': 'Movie {}'.format(movie.movie_name),
        'invoice': str(movie.movie_name),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done', args=[
            movie_name,
            ticket_num,
            attendant_name,
        ])),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'order': movie, 'form':form})

# Handles all the processes needed to make payments on paypal....
