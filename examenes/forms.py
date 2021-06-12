from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Textarea

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields+("email",)


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignupForm(UserCreationForm):   
    class Meta:
        model = User
        fields = ('email', 'first_name','last_name','username')


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre',)
    subject = forms.CharField(label='Asunto')
    email = forms.EmailField(label='Tú Correo electrónico',)
    message = forms.CharField(label='Mensaje',widget=Textarea,)

