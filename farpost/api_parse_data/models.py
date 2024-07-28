from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    advertisement_id = models.IntegerField(unique=True)
    author = models.CharField(max_length=255)
    views = models.IntegerField()
    position = models.IntegerField()

    def __str__(self):
        return self.title
