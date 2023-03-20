from django import forms

from trade.models import Basic


#from .models import Basic


class BasicForm(forms.ModelForm):
    class Meta:
        model = Basic
        valid = True
        fields = '__all__'
