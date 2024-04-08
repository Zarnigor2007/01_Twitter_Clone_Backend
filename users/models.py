from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE,
        related_name='profile',
    )
    image = models.ImageField(upload_to='profile-images/', null=True,blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='profile-images/', null=True, blank=True)
    banner = models.ImageField(upload_to='banners/', null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
class Content(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = 'contents'
    )
    tweet = models.TextField()
    media = models.ImageField(upload_to='content/', null=True, blank=True)

class Like(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_likes'
    )
    content = models.ForeignKey(
        'Content',
        on_delete=models.CASCADE,
        related_name='content_likes'
    )
    class Meta:
        unique_together = ('owner', 'content')