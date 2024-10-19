from django.urls import path

from distributions.apps import DistributionsConfig
from distributions.views import DistributionsListView, DistributionsDetailView

app_name = DistributionsConfig.name

urlpatterns = [
    path("", DistributionsListView.as_view(), name="distributions_list"),
    path(
        "<int:pk>/clients/",
        DistributionsDetailView.as_view(),
        name="distribution_clients",
    ),
]
