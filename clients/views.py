from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ClientsListView(ListView):
    """
    Контроллер для отображения списка клиентов
    """
    pass


class ClientsDetailView(DetailView):
    """
    Контроллер для отображения клиента
    """
    pass


class ClientsCreateView(CreateView):
    """
    Контроллер для создания клиента
    """
    pass


class ClientsUpdateView(UpdateView):
    """
    Контроллер для изменения клиента
    """
    pass


class ClientsDeleteView(DeleteView):
    """
    Контроллер для удаления клиента из списка
    """
    pass
