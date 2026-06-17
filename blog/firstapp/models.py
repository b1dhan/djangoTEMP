from django.db import models

# Create your models here.

class Posts(models.Model):
    POST_CHOICES=[
        ('L','Literature'),
        ('T','Tech'),
        ('S','Social'),
    ]

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'
    author=models.CharField(max_length=25)
    category=models.CharField(max_length=1, choices=POST_CHOICES,default=1)
    title=models.CharField(max_length=200)
    image_url=models.URLField(null=True)
    status=models.CharField(max_length=20)
    content=models.TextField()
    slug=models.CharField(unique=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


