from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder
    
    def save(self, commit=True):
        city_name = self.cleaned_data['name'].capitalize()
        if not City.objects.filter(name=city_name).exists():
            return super().save(commit=commit)
        return None