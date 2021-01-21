from django.db import models


class Coordinates(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    def __str__(self):
        return f"{self.x}, {self.y}"
