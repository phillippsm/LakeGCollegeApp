from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Clubs(models.Model):
    club_name = models.CharField(max_length=50)
    club_head = models.CharField(max_length=60)
    club_location = models.CharField(max_length=30)
    club_description = models.TextField(max_length=250)
    #club_attendees = models.CharField(max_length=50) #bd_column could work here if it's set out like that
    #club_time = models.CharField(max_length=None)
    #club_days = models.CharField(max_length=None)

    # pretty printing
    def __str__(self):
        return self.club_name

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

