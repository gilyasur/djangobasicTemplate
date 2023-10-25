from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Products

def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET','POST','DELETE','PUT'])
def products(request, id = -1):
        if request.method == "GET":
            products = []
            for prod in Products.objects.all():
                    products.append({"Product Id":prod.id, "description":prod.description, "price": prod.price, "category":prod.category})
            return Response(products)
        elif request.method == "POST":
            data = request.data
            prod = Products.objects.create(description=data["description"], price=data["price"], category=data["category"])
            return Response({"done": "success", "product added": prod.description})
        elif request.method == "DELETE" :
            del_prod = Products.objects.filter(id=id)
            if del_prod.exists():
                del_prod.delete()
                return Response({"done": "success", "product removed": "Great"})
            else:
                return Response({"error": "Product not found"})
        elif request.method == "PUT" :
            data = request.data
            upd_prod = Products.objects.filter(id=id)
            if upd_prod.exists():
                upd_prod = upd_prod[0] 
                upd_prod.description = data["description"]
                upd_prod.price = data["price"]
                upd_prod.category = data["category"]
                upd_prod.save()
                return Response({"done": "success", "product updated": upd_prod.description})
            else:
                return Response({"error": "Product not found"})
