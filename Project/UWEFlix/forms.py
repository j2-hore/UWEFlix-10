from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Ticket, Booking


class LoginForm(forms.Form):
    # email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField()

class BookingForm(forms.Form):

    # contact info
    email = forms.EmailField(required=False)

    # Card info
    card_name = forms.CharField(required=False)
    card_number = forms.CharField(required=False)
    card_expiry = forms.CharField(required=False)
    card_cvv = forms.CharField(required=False)



    # Create a field for each available ticket type
    
    def __init__(self, *args, **kwargs):
        available_tickets = kwargs.pop('available_tickets')
        super().__init__(*args, **kwargs)
        for ticket in available_tickets:
          self.fields[f'ticket_{ticket.id}'] = forms.IntegerField(
              label=ticket.name,
              min_value=0,
              initial=0,
              max_value=10,
              required=False,

              # Add price as data attribute to use in JavaScript
              widget=forms.NumberInput(attrs={'data-price': ticket.price})
          )
class DiscountForm(forms.Form):
    UserID = forms.DecimalField
    EmailAddress = forms.CharField
    RequestType = forms.CharField
    RequestValue = forms.CharField

        
    
# Account form for account manager
class AccountForm(forms.Form):
    title = forms.CharField(required=True, label="Account Title")
    card_number = forms.CharField(required=True, label="Card Number")
    expiry_date = forms.CharField(required=True, label="Expiry Date")
    discount_rate = forms.DecimalField(required=True, label="Discount Rate")
    
# Modify Account form for account manager
class ModifyAccountForm(forms.Form):
    title = forms.CharField(required=False, label="Account Title")
    card_number = forms.CharField(required=False, label="Card Number")
    expiry_date = forms.CharField(required=False, label="Expiry Date")
    discount_rate = forms.DecimalField(required=False, label="Discount Rate")


# Add film form for cinema manager
class FilmForm(forms.Form):
    title = forms.CharField(required=True)
    description = forms.CharField(required=True)
    age_rating = forms.CharField(required=True)
    duration = forms.IntegerField(required=True)
    imdb = forms.CharField(required=True)


class ClubForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    contacts = forms.CharField()
    representative = forms.CharField()


class ScreenForm(forms.Form):
    capacity = forms.CharField()


class ShowingForm(forms.Form):
    title = forms.CharField()
    date = forms.CharField()
    time = forms.CharField()

class RequestForm(forms.Form):
    email = forms.CharField()
    request = forms.CharField()

