from django.urls import path
from apps.products.views import *

urlpatterns = [
    path('', ProductAPIView.as_view(), name="api_products"),
    path('create/', ProductCreateAPIView.as_view(), name='product_create_api'),
    path('detail/<int:pk>',ProductDetailAPIView.as_view(),name='product_detail_api'),
    path('update/<int:pk>',ProductUpdateAPIView.as_view(),name='product_update_api'),
    path('delete/<int:pk>',ProductDeleteAPIView.as_view(),name='product_delete_api')
]
