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
    # author=models.CharField(max_length=25)
    category=models.CharField(max_length=1, choices=POST_CHOICES,default=1)
    title=models.CharField(max_length=200)
    image_url=models.URLField(null=True)
    status=models.CharField(max_length=20)
    content=models.TextField()
    slug=models.CharField(unique=True)
    
    from django.conf import settings
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.created_by
    
    def create_slug(self):
        slug=self.title.replace(" ", "-").lower()
        return slug

