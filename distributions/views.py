from django.views.generic import ListView, DetailView
from django.shortcuts import render

from distributions.models import Distribution, Client


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
