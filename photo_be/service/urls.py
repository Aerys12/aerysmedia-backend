from django.urls import path
from service.views import view_services, view_service_categories, view_service_details

app_name = 'service'
urlpatterns = [
    path('list/', view_services.ViewServices.as_view(), name='view_services'),
    path('<int:parent_id>/list/', view_service_categories.ViewServiceCategories.as_view(), name='service_categories'),
    path('<int:id>/details/', view_service_details.ServiceDetails.as_view(), name='service_details'),
    
]