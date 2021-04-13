from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
    title = models.CharField(max_length=500)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.id}.{self.title}'
