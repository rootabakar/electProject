from django.forms import ModelForm
from core.models import User, Cours


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'type', 'password')
        exclude = '__all__'


class CoursForm(ModelForm):

    class Meta:
        model = Cours
        fields = '__all__'
