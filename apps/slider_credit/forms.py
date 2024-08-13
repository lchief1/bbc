from .models import Slider, Credit
from ..catalog import forms


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'image', 'description']

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['name', 'age', 'amount']
