from . import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# We only need four apps: the admin and movie app
