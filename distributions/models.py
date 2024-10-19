from django.db import models

from config.settings import NULLABLE


class Owner(models.Model):
    """
    Модель описывает заказчика рассылки (адресанта рассылки)
    """

    name = models.CharField(max_length=150, verbose_name="Заказчик рассылки")
    owner_email = models.EmailField(verbose_name="почта заказчика", unique=True)

    def __str__(self):
        return f"{self.name} email: {self.owner_email}"

    class Meta:
        verbose_name = "заказчик"
        verbose_name_plural = "заказчики"


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
        Owner, on_delete=models.CASCADE, verbose_name="Заказчик", **NULLABLE
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


class Distribution(models.Model):
    """
    Модель описывает рассылку
    """

    PERIOD_CHOICES = {
        ("daily", "ежедневно"),
        ("weekly", "еженедельно"),
        ("monthly", "ежемесячно"),
    }
    STATUS_CHOICES = {
        ("created", "создана"),
        ("launched", "запущена"),
        ("completed", "завершена"),
    }
    name = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название рассылки"
    )
    first_send = models.DateTimeField(
        verbose_name="Дата и время первой отправки",
        help_text="Укажите дату и время первой отправки",
    )
    period = models.CharField(
        max_length=20,
        choices=PERIOD_CHOICES,
        default="ежедневно",
        verbose_name="Периодичность рассылки",
        help_text="Укажите период рассылки",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="created",
        verbose_name="Статус рассылки",
        help_text="Статус рассылки: завершена, создана, запущена",
    )

    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, verbose_name="Заказчик", **NULLABLE
    )
    clients = models.ManyToManyField(Client, verbose_name="Адресаты")

    def __str__(self):
        return f"Рассылка {self.name}\nДата первой рассылки: {self.first_send}\nПериод рассылки {self.period}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Message(models.Model):
    """
    Модель описывает письмо клиенту
    """

    topic = models.CharField(
        max_length=100,
        verbose_name="Тема письма",
        help_text="Укажите название рассылки",
    )
    body = models.TextField(verbose_name="Тело письма")

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, verbose_name="Укажите адресатов рассылки"
    )

    def __str__(self):
        return f"{self.topic}"

    class Meta:
        verbose_name = "письмо"
        verbose_name_plural = "письма"


class Attempt(models.Model):
    """
    Модель описывает попытку рассылки
    """

    last_attempt = models.DateField(
        verbose_name="Дата и время последней попытки рассылки"
    )
    status = models.BooleanField(verbose_name="Статус попытки", default=False)
    server_answer = models.TextField(verbose_name="Ответ сервера")

    def __str__(self):
        return f"{self.last_attempt} - {self.status}"

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылки"
