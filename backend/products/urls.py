from urllib.parse import urlparse
from django.urls import  path 

from . import views


urlpatterns = [
     path('',views.productCreateView,name="product-lits"),
     path('<int:pk>/',views.productDetailView,name="product-details"),
    path('<int:pk>/update/',views.productUpdateView,name="product-edit"), #class Based views
    path('<int:pk>/delete/',views.productDestroyView), #class Based views
    #path('<int:pk>/',views.ProductDetailAPIView.as_view()),

    ## Function based views
    #path('<int:pk>/delete/',views.product_alt_View),
    #path('<int:pk>/',views.product_alt_View),

    #generic mixin views
    #path('',views.ProductMixinViews.as_view())
]
