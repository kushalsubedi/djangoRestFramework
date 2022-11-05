from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    #url_edit = serializers.SerializerMethodField(read_only=True) # serializing url method 1
    url_edit = serializers.HyperlinkedIdentityField(view_name="product-edit")

    url=serializers.HyperlinkedIdentityField(view_name="product-details",lookup_field="pk") #most common method of serializing url
    class Meta:
        model = Product 
        fields = [
            'user',
            'url',
            'url_edit',
            'title',
            'content',
            'price',
            'sale_price', 
            'my_discount'
        ]
    # def get_url_edit(self,obj): #serializing url method 1
    #     #return f"/api/products/{obj.pk}/"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None 
    #     return reverse("product-edit",kwargs={"pk":obj.pk},request=request)
       
    def get_my_discount(self,obj):
        return obj.get_discount()

        
    def validate_title(self,value):
        qs= Product.objects.filter(title__iexist=value)
        if qs.exists():
            raise serializers.ValidationError("title name already exists")
        return value