

from django.http import Http404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from yaml import serialize
# from django.http import Http404
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
productDetailView = ProductDetailAPIView.as_view()


#function Based API views 
'''

to perform the same CRUD operation as generic View 


'''



@api_view (["GET","POST"])
def product_alt_View(request,pk=None,*args ,**kwargs):
    method = request.method 

    if method == "GET":
        if pk is not None :
            obj = get_object_or_404(Product, pk=pk)
            data=ProductSerializer(obj,many=False).data
            return Response(data)

            #detail view
            # queryset = Product.objects.filter(pk=pk)
            # data=ProductSerializer(queryset, many=True).data
            # if not queryset.exists() :
            #     raise Http404
            # return Response(data)

    queryset= Product.objects.all()
    data = ProductSerializer(queryset, many=True).data
    return Response(data)



    if method == "Post":
        #creating an item
        data=request.data
        serializer = ProductSerializer(data)
        if serializer.is_valid(raise_exception=True):
           title = serializer.validated_data.get('tilte')
           content = serializer.validated_data.get('content') or None
        if content is None :
            content =title
            serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid":"not a good data"})



