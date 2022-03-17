from django.db import models


class Urls(models.Model):
    url = models.TextField()
    name = models.TextField()

    def __str__(self):
        return self.name
