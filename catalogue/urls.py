from django.urls import path
from . import views
from .views import delete


app_name = 'catalogue'

urlpatterns = [
    path('artist/',                       views.artist.index,   name='artist_index'),
    path('artist/create/',                views.artist.create,  name='artist_create'),
    path('artist/<int:artist_id>/',       views.artist.show,    name='artist_show'),
    path('artist/<int:artist_id>/edit/',  views.artist.edit,    name='artist_edit'),
    path('artist/<int:artist_id>/delete/',views.artist.delete,  name='artist_delete'),
    path('profile/delete/<int:pk>/', delete, name='user-delete'),
    path('type/', views.type.index, name='type-index'),
    path('type/<int:type_id>', views.type.show, name='type-show'),
    path('locality/',                       views.locality.index, name='locality_index'),
    path('locality/<int:locality_id>/',     views.locality.show,  name='locality_show'),
    path('price/',            views.price.index, name='price_index'),
    path('price/<int:price_id>/', views.price.show, name='price_show'),
    path('location/', views.location.index, name='location-index'),
    path('location/<int:location_id>', views.location.show, name='location-show'),

]
