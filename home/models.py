from django.db import models as m
from django.contrib.auth.models import User

class IDCard(m.Model): # FYI: It has all the attributes of User such as .is_authenticated etc... since it has inherited from User via onetoone
    user = m.OneToOneField(User, on_delete=m.CASCADE,related_name='me')# this is just to make a onetoone connection between a user and this.
    UserID = m.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return f"{self.user.username}-{self.UserID}"

#how bout linked with the id card only we have balance, in logs, out logs, etc? for starters and we can see groups later.
class Balance(m.Model):
     user = m.ForeignKey(User, on_delete=m.CASCADE,related_name='balance')
     amount = m.DecimalField(max_digits=10, decimal_places=2)

     def __str__(self):
        return f"{self.user}-{self.amount}"
#SHOULD we have log in a different model such that it has datetime and all, would make life easier for reading.

class Income(m.Model): 
    user = m.ForeignKey(User, on_delete=m.CASCADE, related_name='income')  # Changed from OneToOneField to ForeignKey
    Amount = m.DecimalField(max_digits=10, decimal_places=2)
    DTime = m.DateTimeField(null=False)
    FromUser = m.CharField(max_length=1000, null=True, blank=True)  # add in frontend later
    Source = m.CharField(max_length=1000, null=True, blank=True)
    comments = m.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.Amount}-{self.DTime}-{self.Source}-{self.comments}"

class Outgo(m.Model): #automate inputs via a good GUI #WILL NEED TO ADD LOTS MORE, DISCUSS
    user=m.OneToOneField(User, on_delete=m.CASCADE, related_name='Outgo') #sender (you)
    Amount=m.DecimalField(max_digits=10, decimal_places=2)
    DTime=m.DateTimeField(null=False)
    ToUser=m.CharField(max_length=1000,null=True, blank=True) #ADD in frontend later
    Where=m.CharField(max_length=1000,null=True, blank=True)
    Why=m.CharField(max_length=10000,null=True, blank=True) #LATER FIGURE OUT MONEY DRAIN AREA THING
    comments=m.CharField(max_length=10000,null=True, blank=True) #TODO ADD reciept pic

    def __str__(self):
        return f"{self.user}-{self.Amount}-{self.DTime}-{self.Where}-{self.Why}-{self.comments}"