from django import forms

from api.models.city import City


class CityForm(forms.ModelForm):
    class Meta():
        model = City
        fields = ('name',)