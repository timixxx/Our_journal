from django.db import models
from django.utils import timezone


class Record(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=60)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Records"

