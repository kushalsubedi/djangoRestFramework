

from django.http import Http404
from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from yaml import serialize
# from django.http import Http404
from .models import Product
from .serializers import ProductSerializer

# Class based generic views 

class productListCreateAPIView(generics.ListCreateAPIView):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer
     def perform_create(self, serializer):
         title = serializer.validated_data.get('tilte')
         content = serializer.validated_data.get('content') or None
         if content is None :
             content =title
         serializer.save(content=content)
      
productCreateView =productListCreateAPIView.as_view()  #changing class based views as function based typo

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
productDetailView = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'

    def Perform_update(self, serializer):
        instance=serializer.save()
        if not instance.content:
            instance.content=instance.title
        
productUpdateView = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field ='pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

    
        
productDestroyView = ProductDestroyAPIView.as_view()
#function Based API views 


'''

to perform the same CRUD operation as genericmodel View 


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
  
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
           title = serializer.validated_data.get('tilte')
           content = serializer.validated_data.get('content') or None
        if content is None :
            content =title
            serializer.save(content=content)
        return Response(serializer.data)
    return Response({"invalid":"not a good data"})



# Rest_API Mixins and generic API views


class ProductMixinViews(
    mixins.CreateModelMixin, #it provides create method
    mixins.ListModelMixin, # it displays all data 
    mixins.RetrieveModelMixin , # provide details With respect to lookup_pk
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'

    def get(self,request,*args,**kwargs): #HTTP->get
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs): #HTTP -> post
        return self.create (request,*args,**kwargs)




