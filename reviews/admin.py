from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReaviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    pass