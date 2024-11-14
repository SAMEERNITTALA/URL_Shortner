from django.db import models

class URL(models.Model):
    original_url = models.URLField(max_length=500)
    shortened_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.shortened_url} -> {self.original_url}"

