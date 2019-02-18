from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    discription = models.CharField(max_length=500, default='')
    city = models.CharField(max_length=500, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image=models.ImageField(blank=True, upload_to='profile_image')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Userprofile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)