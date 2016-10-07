from django.conf.urls import url

from .views import Getstates, Getcities

urlpatterns = [
    url(r'^search/states$',
        Getstates.as_view(),
        name='search-states-view'),

    url(r'^search/cities$',
        Getcities.as_view(),
        name='search-cities-view'),
]
