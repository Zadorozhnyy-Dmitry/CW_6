from django.contrib import admin

from distributions.models import Owner, Distribution, Client, Message, Attempt


# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "owner_email",
    )


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "client_email",
        "comments",
        "owner",
    )
    list_filter = ("owner",)


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
