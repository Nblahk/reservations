from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('artist/',                       views.artist.index,   name='artist_index'),
    path('artist/create/',                views.artist.create,  name='artist_create'),
    path('artist/<int:artist_id>/',       views.artist.show,    name='artist_show'),
    path('artist/<int:artist_id>/edit/',  views.artist.edit,    name='artist_edit'),
    path('artist/<int:artist_id>/delete/',views.artist.delete,  name='artist_delete'),
]
