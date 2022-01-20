
from django import forms
from django.db.models import fields
from tracker.models import Item



class ItemModelForm(forms.ModelForm):
    class Meta():
        model = Item
        fields = (
            'name',
            'quantity'
        )
        

