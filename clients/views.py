from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from clients.models import Client


class ClientsListView(ListView):
    """
    Контроллер для отображения списка клиентов
    """
    model = Client


class ClientsCreateView(CreateView):
    """
    Контроллер для создания клиента
    """
    model = Client
    fields = ('name', 'client_email', 'comments',)
    success_url = reverse_lazy('clients:clients_list')


class ClientsUpdateView(UpdateView):
    """
    Контроллер для изменения клиента
    """
    model = Client
    fields = ('name', 'client_email', 'comments',)
    success_url = reverse_lazy('clients:clients_list')


class ClientsDeleteView(DeleteView):
    """
    Контроллер для удаления клиента из списка
    """
    model = Client
    success_url = reverse_lazy('clients:clients_list')
