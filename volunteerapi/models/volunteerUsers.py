from django.contrib.auth.models import User
from django.db import models

class VolunteerUsers(models.Model):
    bio = models.CharField(max_length=2000)
    profile_image_url = models.URLField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    is_business = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    volunteer_username = models.CharField(max_length=64)
    favorite = models.ManyToManyField('JobPosts', through='Favorites', related_name='volunteer')
    cause_area = models.ManyToManyField('CauseAreas', through='UserCause', related_name='user')