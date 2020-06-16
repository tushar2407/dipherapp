from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=256)
    file=models.FileField(upload_to='files/')
    #url=models.FilePathField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    #cover=models.ImageField(default=NULL)
    encrypted=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    """def __init__(self, *args, **kwargs):
        self.user=user"""
    def delete(self,*args,**kwargs):
        self.file.delete()
        super().delete(*args,**kwargs)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    bio=models.TextField(max_length=500, blank=True)
    location=models.CharField(max_length=100, blank=True)
    birth_date=models.DateField(null=True, blank=True)

@receiver(post_save,sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()