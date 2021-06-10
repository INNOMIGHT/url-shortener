from django.db import models


class ShortUrls(models.Model):

    short_url = models.CharField(max_length=20)
    long_url = models.URLField('URL', unique=True, max_length=255)

