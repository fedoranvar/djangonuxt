from djongo import models
# from datetime import datetime
from django.utils.timezone import now as datetime_now


class Claim(models.Model):
    title = models.CharField(max_length=80)

    class DocType(models.TextChoices):
        JAN = "1", "DGSTR"
        FEB = "2", "STREA"
        MAR = "3", "OSTR"

    doc_type = models.CharField(
        max_length=2, choices=DocType.choices, default=DocType.JAN
    )

    priority = models.IntegerField(default=1)
    create_date = models.DateTimeField(default=datetime_now)
    image = models.BinaryField(blank=True)
    attachment = models.FileField(upload_to="uploads/", blank=True)
    is_special = models.BooleanField(default=False)


# Create your models here.
