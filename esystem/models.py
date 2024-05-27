from django.db import models

# Create your models here.


class HazardousWasteSystem(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    electronic_manifest = models.BooleanField(
        default=False,
    )
    data_plus_image_manifest = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = "Hazardous Waste System"
        verbose_name_plural = "Hazardous Waste Systems"

    def __str__(self):
        return self.name
