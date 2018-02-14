from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone

class Trainee(models.Model):
    name = models.ForeignKey(User,on_delete = models.CASCADE)
    age = models.IntegerField(default = 0)
    email = models.EmailField()
    phone_number = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.name)

def create_profile(sender,**kwargs):
    if kwargs['created']:
        trainee_profile = Trainee.objects.create(name = kwargs['instance'])

post_save.connect(create_profile,sender = User)


class Exercise(models.Model):
    tip = models.CharField(max_length = 400)
    workout = models.TextField()
    start_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.tip
