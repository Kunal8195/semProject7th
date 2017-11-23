from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Customers

class MyRegistrationForm(UserCreationForm):
      email=forms.EmailField(required=True)
      firstname=forms.CharField(max_length=10,required=True)
password1 = forms.CharField(widget=forms.PasswordInput)
password2 = forms.CharField(widget=forms.PasswordInput)
      
class Meta:
       model =User
       fields = ('username','email','firstname','password1','password2')

       def save(self,commit=True):
            user = super(UserCreationForm,self).save(commit = False)
            user.email = self.cleaned_data['email']
            user.firstname = self.cleaned_data['firstname']
	    user.password = self.cleaned_data['password2']
			
            if commit:
              user.save()
 
            return user   

class Customers_form(forms.ModelForm):

    class Meta:
        model = Customers
        fields = ('customernumber','customername','contactlastname')

			