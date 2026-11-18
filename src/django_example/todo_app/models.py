from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} — {self.author}"