from django.db import models
from django.contrib.auth.models import User #, Permission

# Create your models here.


################################################################################
##############################    Authorization   ##############################
################################################################################



################################################################################
##############################      DB Models     ##############################
################################################################################


# Old User class. Now using User class from django contrib.auth.models!
# User descriptions: need one-to-one relationship such as:
class UserDescription(models.Model):
    ref = models.OneToOneField(User)
    about = models.CharField(max_length=1000)
    affiliation = models.CharField(max_length=100)
    #picture = models.FileFIeld() #TODO: user correct argument options
    
    def __str__(self):
        return self.ref


class Keyword(models.Model):
    word = models.CharField(max_length=25)
    
    def __str__(self):
        return self.word
    

class Protocol(models.Model):
    publisher = models.ForeignKey(User, blank=True) # who published the protocol
    pub_date = models.DateTimeField(auto_now=True) #sets field to now everytime it is saved. use auto_now_add to only add time when object first created
    title = models.CharField(max_length=100) # title of the protocol
    description = models.CharField(max_length=500) # short description for the protocol when browsing
    #keywords = models.CharField(max_length=500)#many-to-many not supported error
    keywords = models.ManyToManyField(Keyword, blank=True) # keywords for searching for protocols, not required
    text = models.TextField() # all details and descriptions for the protocol
    #calc_methods = models.Field(CustomField) # calculator part - later! Within: need list of parameters and dependencies
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    protocol = models.ForeignKey(Protocol) # many comments for one protocol
    user = models.ForeignKey(User) # many comments for one user
    pub_date = models.DateTimeField('date published')
    text = models.TextField()
    
    def __str__(self):
        return self.pub_date # can change to something more useful
    

class Rating(models.Model):
    protocol = models.ForeignKey(Protocol) # many ratings for one protocol
    user = models.ForeignKey(User) # many given ratings for one user
    integer = models.PositiveSmallIntegerField() #rate between 1-5, e.g.
    text = models.TextField() # rant space for the rating
    
    def __str__(self):
        return user # can change to something more useful

