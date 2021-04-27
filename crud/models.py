from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
