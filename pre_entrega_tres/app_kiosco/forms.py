from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Create_new_person(forms.Form):
    name = forms.CharField(label="Nombre", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=200)

class Create_new_product(forms.Form):
    name = forms.CharField(max_length=200)
    size = forms.IntegerField()
    code = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'User'}))
    email = forms.EmailField(label='E-mail', required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email@'}))
    password1 = forms.CharField(label='Contraseña', required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Repetir contraseña', required=True, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'FirstName'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'LastName'}))
    address = forms.CharField(label="Direccion", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2','first_name', 'last_name', 'address']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar E-mail', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'FirstName'}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'LastName'}))
    address = forms.CharField(label="Direccion", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','first_name', 'last_name', 'address']
        help_texts = {k:"" for k in fields}
    
""" class AvatarFormulario(forms.Form):
    pass """

""" class news_letter(forms.Form):
    email = forms.EmailField(label=forms.TextInput(attrs={'value':'E-mail', 'class':"form-label", 'for':"form5Example21"}), widget=forms.TextInput(attrs={'type':"email", 'name':'newletter', 'id':"form5Example21", 'class':"form-control", 'placeholder':'Email'})) """