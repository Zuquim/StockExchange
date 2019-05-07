from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offers', views.offers, name='offers'),
    path('offer/<int:offer_id>', views.offer_details, name='offer_details'),
    path('make_offer', views.make_offer, name='make_offer'),
]