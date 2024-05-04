from django.urls import path
from gallery.views import create_gallery_view, gallery_view, galleries_list_view, gallery_update_view, delete_gallery_view, gallery_images_view, upload_image_view, delete_image_view


app_name = 'gallery'
urlpatterns = [
    path('create/', create_gallery_view.GalleryCreateView.as_view(), name='create-gallery'),
    path('<int:pk>/details/', gallery_view.GalleryDetailView.as_view(), name='gallery-detail'),
    path('list/', galleries_list_view.GalleryListView.as_view(), name='gallery-list'),
    path('<int:pk>/update/', gallery_update_view.GalleryUpdateView.as_view(), name='gallery-update'),
    path('<int:pk>/delete/', delete_gallery_view.GalleryDeleteView.as_view(), name='gallery-delete'),
    path('<int:gallery_id>/images/upload/', upload_image_view.ImageUploadView.as_view(), name='image-upload'),
    path('<int:gallery_id>/images/', gallery_images_view.GalleryImagesView.as_view(), name='gallery-images'),
    path('<int:gallery_id>/images/<int:image_id>/delete/', delete_image_view.ImageDeleteView.as_view(), name='image-delete'),
]