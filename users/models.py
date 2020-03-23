from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=40)
    role_description = models.CharField(max_length=40)

    def __str__(self):
        return self.role_name


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")
    phone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.user.email