from django.contrib import admin
from django import forms
from .models import Gallery, Image
#from .widgets import MultipleFileInput


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class MultipleFileInput(forms.FileInput):
    def render(self, name, value, attrs=None, renderer=None):
        if attrs is None:
            attrs = {}
        attrs['multiple'] = 'multiple'
        return super().render(name, value, attrs)

class MultiImageUploadForm(forms.ModelForm):
    image_files = forms.FileField(widget=MultipleFileInput, required=False, label='Image Files')

    class Meta:
        model = Gallery
        fields = '__all__'

    def save(self, commit=True):

        instance = super().save(commit=False)
        for file in self.files.getlist('image_files'):
            Image.objects.create(gallery=instance, image_file=file)
        if commit:
            instance.save()
        return instance

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    form = MultiImageUploadForm

    

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image)
