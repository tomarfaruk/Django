from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    post = models.CharField(max_length=500)
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post

class Friend(models.Model):
    user = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='woner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, create = cls.objects.get_or_create(current_user=current_user)
        friend.user.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, create = cls.objects.get_or_create(current_user=current_user)
        friend.user.remove(new_friend)