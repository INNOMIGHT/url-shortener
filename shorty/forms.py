from django.forms import ModelForm
from .models import ShortUrls


class CleanUrlForm:
    def clean_your_url_field(self):
        return self.cleaned_data['long_url'].lower()


class UrlForm(CleanUrlForm, ModelForm):

    class Meta:

        model = ShortUrls
        fields = ['long_url']
