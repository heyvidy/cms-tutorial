from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
