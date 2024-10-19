from django.urls import path

from distributions.apps import DistributionsConfig
from distributions import views

app_name = DistributionsConfig.name

urlpatterns = [
    path("", views.index, name="distributions_examples"),
    path("examples/clients/", views.clients_list_examples, name="distributions_examples_clients"),
    path("list/", views.DistributionsListView.as_view(), name="distributions_list"),
    path(
        "<int:pk>/clients/",
        views.DistributionsDetailView.as_view(),
        name="distribution_clients",
    ),
]
