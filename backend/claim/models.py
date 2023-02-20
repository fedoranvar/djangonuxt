from django import forms
# from datetime import datetime
from django.utils.timezone import now as datetime_now
from djongo import models


class Document(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        abstract = True


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ("name",)


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

    documents = models.ArrayField(
        model_container=Document, model_form_class=DocumentForm,  null=True, default=list()
    )
