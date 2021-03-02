from django.db import models
import datetime


# Create your models here.
class Person(models.Model):
    current_time = datetime.datetime.now().timestamp()

    def __default_person_friends():
        return dict(persons=[])

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=100)
    avatar = models.URLField(default="")
    birthday = models.CharField(max_length=10)
    tagline = models.CharField(max_length=200, default="")
    slug = models.CharField(max_length=100, unique=True)
    created = models.FloatField(default=current_time)
    updated = models.FloatField(default=current_time)

    def __str__(self):
        return "id:"+str(self.pk) + ", " + self.first_name + " " + self.last_name+ ", " + self.email

class Token(models.Model):
    token = models.CharField(max_length=100)
    account = models.IntegerField()
    created = models.DateTimeField()

    def __str__(self):
        return "person_id: "+str(self.account)