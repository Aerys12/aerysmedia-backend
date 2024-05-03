from django.urls import path
from gallery.views import create_gallery_view, gallery_view, galleries_list_view, gallery_update_view, delete_gallery_view

app_name = 'gallery'
urlpatterns = [
    path('create/', create_gallery_view.GalleryCreateView.as_view(), name='create-gallery'),
    path('<int:pk>/details/', gallery_view.GalleryDetailView.as_view(), name='gallery-detail'),
    path('list/', galleries_list_view.GalleryListView.as_view(), name='gallery-list'),
    path('<int:pk>/update/', gallery_update_view.GalleryUpdateView.as_view(), name='gallery-update'),
    path('<int:pk>/delete/', delete_gallery_view.GalleryDeleteView.as_view(), name='gallery-delete'),
]