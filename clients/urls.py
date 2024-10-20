from django.urls import path

from clients.apps import ClientsConfig
from clients import views

app_name = ClientsConfig.name

urlpatterns = [
    path('', views.ClientsListView.as_view(), name='clients_list'),
    path('create/', views.ClientsCreateView.as_view(), name='client_create'),
    path('edit/<int:pk>/', views.ClientsUpdateView.as_view(), name='client_edit'),
    path('delete/<int:pk>/', views.ClientsDeleteView.as_view(), name='client_delete'),
]
