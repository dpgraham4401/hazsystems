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
        help_text="Does the system support electronic manifests?",
        blank=True,
    )
    data_plus_image_manifest = models.BooleanField(
        default=False,
        help_text="Does the system support data plus image manifests?",
        blank=True,
    )

    class Meta:
        verbose_name = "Hazardous Waste System"
        verbose_name_plural = "Hazardous Waste Systems"

    def __str__(self):
        return self.name
