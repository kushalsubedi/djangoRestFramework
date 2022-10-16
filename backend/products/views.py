

from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer


class productListCreateAPIView(generics.ListCreateAPIView) :
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('tilte')
        content = serializer.validated_data.get('content') or None

        if content is None :
            content =title
        serializer.save(content=content)
       

   
        
    


productCreateView =productListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
#productDetailView = ProductDetailAPIView.as_view()


