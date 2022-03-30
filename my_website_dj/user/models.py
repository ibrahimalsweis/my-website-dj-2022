from email.mime import image
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    img = models.ImageField(default='default.jpg',upload_to='users_img_profile')
    user = models.OneToOneField(User,on_delete=models.CASCADE )

    def __str__(self):
        return f'صورة الملف الشخصي للمستخدم {self.user}'
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.img.path)
        if img.width >5500 or img.height > 5500 :
            img.thumbnail((250,250))
            img.save(self.img.path)
def create_profile(sender,**args):
    if args['created']:
        Profile.objects.create(user=args['instance'])
post_save.connect(create_profile,sender=User)