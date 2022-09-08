from django.db import models


class TEST_MODEL(models.Model):
    context = models.CharField(max_length=100, null=True)
