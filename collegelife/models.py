from django.db import models

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

