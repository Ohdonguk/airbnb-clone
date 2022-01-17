from django.contrib import admin
from . import models


@admin.register(models.List)
class listAdmin(admin.ModelAdmin):

    """ List Admin Definition """

    list_display = (
        "name",
        "user",
        "count_room",
    )

    search_fields = ("name",)

    filter_horizontal = ("rooms",)