from django.db import models


# Create your models here.
class Waste(models.Model):
    """A waste type"""

    name = models.CharField(max_length=100)
    description = models.TextField()
    code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class WasteTag(models.Model):
    """A tag for a waste type"""

    name = models.CharField(max_length=100)
    waste = models.ManyToManyField(Waste, related_name="tags")

    def __str__(self):
        return self.name
