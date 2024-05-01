from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cars/',views.cars,name='cars'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('workshop/',views.workshop,name='workshop'),
    path('spareparts/',views.spareparts,name='spareparts'),
    path('cardetails/',views.cardetails,name='cardetails'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)