from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        length = len(self.body)
        if length > 50:
            return self.body[:50] + '...'
        return self.body
