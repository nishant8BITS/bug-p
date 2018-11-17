from django.conf.urls import url
from .views import graph, number_of_graph

urlpatterns = [
    url(r'^$', graph, name='graphs'),
    url(r'^api/data', number_of_graph, name='number_of_graph'),
]