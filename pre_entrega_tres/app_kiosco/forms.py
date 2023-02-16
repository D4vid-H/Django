from django import forms

class Create_new_person(forms.Form):
    name = forms.CharField(label="Nombre", max_length=150),
    last_name = forms.CharField(label="Apellido", max_length=200)