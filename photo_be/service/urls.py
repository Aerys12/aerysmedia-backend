from django.urls import path
from service.views import view_services, view_service_categories, view_service_details, view_all_service_categories, view_services_simple

app_name = 'service'
urlpatterns = [
    path('list/', view_services.ViewServices.as_view(), name='view_services'),
    path('simple/list/', view_services_simple.ViewServices.as_view(), name='view_services'),
    path('<int:parent_id>/list/', view_service_categories.ViewServiceCategories.as_view(), name='service_categories'),
    path('<int:id>/details/', view_service_details.ServiceDetails.as_view(), name='service_details'),
    path('categories/list/', view_all_service_categories.ViewAllServiceCategories.as_view(), name='all_service_categories'),
    
]