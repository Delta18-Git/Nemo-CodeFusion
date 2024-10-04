from django.db import models as m
from django.contrib.auth.models import User

class IDCard(m.Model): # FYI: It has all the attributes of User such as .is_authenticated etc... since it has inherited from User via onetoone
    user = m.OneToOneField(User, on_delete=m.CASCADE,related_name='me')# this is just to make a onetoone connection between a user and this.
    UserID = m.CharField(max_length=500,null=False,blank=False)
    def __str__(self):
        return f"{self.user.username}-{self.UserID}"