#uncteams app models.py

from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    headcoach = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=200)
    
    class Meta(object):
        verbose_name_plural = "Teams",
        #ordering = ('name')
        
    def __unicode__(self):
        return U'%s | %s' %(self.name)
        
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Team, self).save(*args, **kwargs)
            


class Athlete(models.Model):
    name = models.CharField(unique=False, max_length=50)
    team = models.ForeignKey(Team)
    year = models.CharField(unique=False, max_length=20)
    hometown = models.CharField(unique=False, max_length=50, null=True)
    imageURL = models.CharField(unique=False, max_length=200)
    pr5k = models.CharField(unique=False, max_length=10, null=True)
    position = models.CharField(unique=False, max_length=10, null=True)
    height = models.IntegerField(unique=False, max_length=5, null=True)
    weight = models.IntegerField(unique=False, max_length=3, null=True)
    highschool = models.CharField(unique=False, max_length=40, null=True)
    hobbies = models.CharField(unique=False, max_length=50, null=True)
    favfood = models.CharField(unique=False, max_length=20, null=True)
    favtv = models.CharField(unique=False, max_length=20, null=True)
    favbook = models.CharField(unique=False, max_length=20, null=True)
    favartist = models.CharField(unique=False, max_length=20, null=True)
    
    class Meta(object):
        verbose_name_plural = "Athletes"
        #ordering = ('name')
    
    def __unicode__(self):
        return U'%s %s' %(self.name)

class Coach(models.Model):
    name = models.CharField(unique=False, max_length=50)
    team = models.ForeignKey(Team)
    position = models.CharField(unique=False, max_length=50)
    yearsexp = models.IntegerField(unique=False, max_length=3, null=True)
    emailAdd = models.CharField(unique=False, max_length=50, null=True)
    bio = models.CharField(unique=False, null=True, max_length=300)

    
    class Meta(object):
        verbose_name_plural = "Coaches"
        #ordering = ('name')
    
    def __unicode__(self):
        return U'%s %s' %(self.name)