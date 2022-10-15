from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

from products.models import Product
# Create your views here.


@api_view(["post"])# converting normal view to an REST api veiw 
def api_home (request, *args,**kwargs): 
    '''
    Django Rest framework api veiw 
    '''


    '''
    in pure django method 
 
    # if request.method != 'POST':
    #     return Response ({'details' : 'Post not allowed', status = 400})
    '''
    # this is equivalent to the @api_view ["POST"] / ["get"] method

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance=serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid data"},status=405.40)

    # instance= Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
        
    #     #data = model_to_dict (model_data,fields=['id' ,'title','price'] #only this fields are allowes others are restricted
    #     data = ProductSerializer(instance).data 
    # return Response(data)