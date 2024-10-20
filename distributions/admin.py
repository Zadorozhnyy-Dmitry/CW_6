from django.contrib import admin

from distributions.models import Distribution, Message, Attempt


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "first_send",
        "period",
        "status",
        "owner",
    )
    list_filter = ("owner",)
    ordering = ("first_send",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "topic",
        "body",
        "client",
    )
    list_filter = ("client",)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_attempt",
        "status",
        "server_answer",
    )
