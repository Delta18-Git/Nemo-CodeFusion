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

from decimal import Decimal

class Loan(m.Model): #TODO IMP FIGURE OUT AUTOMATION!!!
    user = m.ForeignKey(User, on_delete=m.CASCADE, related_name='Loan') 
    loan_amount = m.DecimalField(max_digits=10, decimal_places=2)  # Excluding down payment
    annual_interest_rate = m.DecimalField(max_digits=5, decimal_places=2)  # In percentage
    loan_tenure = m.IntegerField(null=False)  # In years

    def calculate_emi(self):
        # Convert DecimalFields to floats for calculation
        loan_amount = float(self.loan_amount)
        annual_interest_rate = float(self.annual_interest_rate)
        loan_tenure_years = self.loan_tenure

        # Calculate monthly interest rate
        monthly_rate = (annual_interest_rate / 12) / 100
        tenure_months = loan_tenure_years * 12

        # EMI formula
        emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** tenure_months) / (((1 + monthly_rate) ** tenure_months) - 1)
        
        return Decimal(emi)  # Return as Decimal to match database field types

    def __str__(self):
        # Display calculated EMI
        return f"User: {self.user}, EMI: {self.calculate_emi()}, Loan Amount: {self.loan_amount}, Tenure: {self.loan_tenure}, Interest Rate: {self.annual_interest_rate}"


class Subscriptions(m.Model): #TODO IMP Figure out the automation!!!
    user = m.ForeignKey(User, on_delete=m.CASCADE, related_name='Sub') 
    sub_amount = m.DecimalField(max_digits=10, decimal_places=2)
    sub_tenure = m.IntegerField(null=False)  #in months

    def __str__(self):
        return f"User: {self.user}, Loan Amount: {self.sub_amount}, Tenure: {self.sub_tenure}"

