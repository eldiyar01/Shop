from django.urls import path, include
from .views import main, all_subcategories, dtl_furniture, checkout

app_name = 'furniture'
urlpatterns = [
    path('', main, name='main'),
    path('<int:pk>/', dtl_furniture, name='sng_furniture'),
    path('checkout/', checkout, name='checkout'),
]