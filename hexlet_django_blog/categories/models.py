from django.db import models


class Category(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.CharField('description', max_length=255)

    def __str__(self):
        return self.name
