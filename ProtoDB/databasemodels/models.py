from django.db import models
from django.contrib.auth.models import User #, Permission

# Create your models here.


################################################################################
##############################    Authorization   ##############################
################################################################################



################################################################################
##############################      DB Models     ##############################
################################################################################



# User descriptions: need one-to-one relationship such as:
class UserDescription(models.Model):
    ref = models.OneToOneField(User)
    about = models.CharField(max_length=1000)
    affiliation = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.ref

    

class Protocol(models.Model):
    publisher = models.ForeignKey(User, blank=True) # who published the protocol
    pub_date = models.DateTimeField(auto_now=True) #sets field to now everytime it is saved. use auto_now_add to only add time when object first created
    title = models.CharField(max_length=100) # title of the protocol
    description = models.CharField(max_length=1000) # short description for the protocol when browsing
    
    text = models.TextField() # all details and descriptions for the protocol
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return 'protocol', (self.slug,)
    
