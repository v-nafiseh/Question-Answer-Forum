from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='defalt.jpg', upload_to='prfile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
        
    