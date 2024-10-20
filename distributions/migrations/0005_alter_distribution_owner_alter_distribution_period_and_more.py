# Generated by Django 4.2 on 2024-10-20 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("distributions", "0004_remove_client_owner_alter_distribution_clients"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("clients", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distribution",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Заказчик",
            ),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="period",
            field=models.CharField(
                choices=[
                    ("monthly", "ежемесячно"),
                    ("daily", "ежедневно"),
                    ("weekly", "еженедельно"),
                ],
                default="ежедневно",
                help_text="Укажите период рассылки",
                max_length=20,
                verbose_name="Периодичность рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="distribution",
            name="status",
            field=models.CharField(
                choices=[
                    ("completed", "завершена"),
                    ("created", "создана"),
                    ("launched", "запущена"),
                ],
                default="created",
                help_text="Статус рассылки: завершена, создана, запущена",
                max_length=20,
                verbose_name="Статус рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="clients.client",
                verbose_name="Укажите адресатов рассылки",
            ),
        ),
        migrations.DeleteModel(
            name="Client",
        ),
        migrations.DeleteModel(
            name="Owner",
        ),
    ]
