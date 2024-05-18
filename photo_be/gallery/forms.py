from django import forms
from gallery.widgets import MultipleFileInput

class MultiImageUploadForm(forms.ModelForm):
    images = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True}), required=True)
