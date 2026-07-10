from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    color = models.CharField(max_length=20, default="#3788d8")

    def __str__(self):
        return self.title