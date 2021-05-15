from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pictures'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_results, name='search'),
    path('location/<str:location>', views.image_location, name='location'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)