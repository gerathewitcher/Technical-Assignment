from django.db import models


# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.id}.{self.title}'
