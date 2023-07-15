from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('account.urls')),
    path('guides/', include('guides.urls')),
    path('car_rental/', include('car_rental.urls')),
    path('housing/', include('housing.urls')),
    path('bookings/', include('housing.urls')),
    path('articles/', include('articles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
