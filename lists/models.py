from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_room(self):
        return self.rooms.count()

    count_room.short_description = "Number of Rooms"