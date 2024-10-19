from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from distributions.models import Distribution
from django.http import HttpResponse


def index(request):
    """
    Контроллер отображения главной страницы с образцами
    """
    return render(request, 'distributions/distribution_examples.html')


def clients_list_examples(request):
    """
    Контроллер отображения образца со списком клиентов
    """
    return render(request, 'distributions/distribution_examples_clients.html')


class DistributionsListView(ListView):
    """
    Контролер для списка рассылок
    """
    model = Distribution


class DistributionsDetailView(DetailView):
    """
    Контроллер для отображения списка адресатов одной рассылки
    """

    model = Distribution


class DistributionsCreateView(CreateView):
    """
    Контроллер создания рассылки
    """
    pass


class DistributionsUpdateView(UpdateView):
    """
    Контроллер изменения рассылки
    """
    pass


class DistributionsDeleteView(DeleteView):
    """
    Контроллер удаления рассылки
    """
    pass
