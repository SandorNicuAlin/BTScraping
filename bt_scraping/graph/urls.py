from django.urls import path
from graph.views import bt_graph

urlpatterns = [
    path('bt', bt_graph, name='bt-graph'),
]
