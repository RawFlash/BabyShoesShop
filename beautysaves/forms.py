from django import forms
from .models import *


class GirlsForm(forms.ModelForm):

    class Meta:
        model = Girls
        exclude = [""]
