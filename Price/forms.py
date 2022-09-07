from .models import Data , Ticker
from django import forms


class DataCreateForm(forms.ModelForm):
    class Meta:
        model = Ticker
        fields = '__all__'



class PriceCreateForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'