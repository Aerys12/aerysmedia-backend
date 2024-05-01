from django.urls import path
from gallery.views import create_gallery_view

app_name = 'gallery'
urlpatterns = [
    path('create/', create_gallery_view.GalleryCreateView.as_view(), name='create-gallery'),
]