from django import forms

from core.models import Reclamation


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ('motif', 'cours', 'preuve')
        exclude = '__all__'
