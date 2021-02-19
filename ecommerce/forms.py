from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order,Ticket


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']