from django.forms import ModelForm
from core.models import User, Reclamation, Cours, Heure
from django import forms


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'type', 'password')
        exclude = '__all__'


class CoursForm(ModelForm):

    class Meta:
        model = Cours
        fields = '__all__'


class HeureForm(ModelForm):

    class Meta:
        model = Heure
        fields = '__all__'
        widgets = {
            'horaire': forms.TextInput(attrs={'placeholder': '00:30 - 20:00'}),
        }
