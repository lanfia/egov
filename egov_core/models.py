from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Partner(models.Model):
    partner_code = models.CharField('Partner Code',max_length=5,help_text='Partner Short Code eg. UNDP')
    partner_name =  models.CharField('Partner Name',max_length=150)

    def __str__(self):
        return self.partner_code