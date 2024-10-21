from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import render
from django.urls import reverse_lazy

from distributions.models import Distribution


def index(request):
    """
    Контроллер отображения главной страницы с образцами
    """
    return render(request, "distributions/distribution_examples.html")


def clients_list_examples(request):
    """
    Контроллер отображения образца со списком клиентов
    """
    return render(request, "distributions/distribution_examples_clients.html")


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

    model = Distribution
    fields = ("name", "first_send_date", "first_send_time", "period", "clients")
    success_url = reverse_lazy("distributions:distributions_list")


class DistributionsUpdateView(UpdateView):
    """
    Контроллер изменения рассылки
    """

    model = Distribution
    fields = ("name", "first_send_date", "first_send_time", "period", "clients")
    success_url = reverse_lazy("distributions:distributions_list")


class DistributionsDeleteView(DeleteView):
    """
    Контроллер удаления рассылки
    """

    model = Distribution
    success_url = reverse_lazy("distributions:distributions_list")
