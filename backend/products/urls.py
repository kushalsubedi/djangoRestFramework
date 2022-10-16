from urllib.parse import urlparse
from django.urls import  path 

from . import views


urlpatterns = [
    # path('',views.productCreateView),
    # path('<int:pk>/',views.ProductDetailAPIView.as_view()),
#    path('<int:pk>/',views.productDetailView),


    path('',views.product_alt_View),
    path('<int:pk>/',views.product_alt_View),
]
