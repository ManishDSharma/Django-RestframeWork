import json
from django.forms.models import model_to_dict
from pyexpat import model
from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializers


@api_view(["GET","PSOT"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance,fields=['id','title','price','sale_price'])
        data = ProductSerializers(instance).data

    return Response(data)