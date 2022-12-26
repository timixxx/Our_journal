from django.db import models
from django.utils import timezone


class Record(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=60, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Records"

