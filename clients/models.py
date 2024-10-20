from django.db import models

from config.settings import NULLABLE
from users.models import User


class Client(models.Model):
    """
    Модель описывает клиента сервиса (адресат рассылки)
    """

    name = models.CharField(
        max_length=150,
        verbose_name="Ф.И.О",
        help_text="Укажите фамилию, имя и отчество клиента",
        **NULLABLE,
    )
    client_email = models.EmailField(
        verbose_name="email клиента", help_text="Укажите электронный адрес клиента"
    )
    comments = models.CharField(
        max_length=150, verbose_name="Комментарий", help_text="Комментарий", **NULLABLE
    )

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Заказчик", **NULLABLE
    )

    def __str__(self):
        return f"{self.client_email} ({self.name})"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = (
            "id",
            "client_email",
        )
