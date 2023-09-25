from django import forms
from core.models import Reclamation, Cours


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        exclude = ('etat', 'etudiant')
        fields = '__all__'

    cours = forms.ModelChoiceField(queryset=Cours.objects.all())
