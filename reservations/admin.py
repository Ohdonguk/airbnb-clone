from django.contrib import admin
from . import models


@admin.register(models.reservations)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    pass