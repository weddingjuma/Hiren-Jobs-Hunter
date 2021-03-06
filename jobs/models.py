from django.db import models


class Keyword(models.Model):
    keyword = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Job(models.Model):
    url = models.URLField()

