from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    CATEGORY_CHOICES = [
        ('Politics', 'Politics'),
        ('Business', 'Business'),
        ('Technology', 'Technology'),
        ('Sports', 'Sports'),
        ('Entertainment', 'Entertainment'),
        ('World', 'World'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='news_photos/', blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
