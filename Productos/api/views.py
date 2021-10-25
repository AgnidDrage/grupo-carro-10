from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Distributor, Products
import json as js

# Create your views here.
class productsView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=0):

        # Devuelve producto especifico.
        if id > 0:
            if Products.objects.filter(id=id).exists():
                product = Products.objects.get(id=id)
                data = {
                    'id': product.id,
                    'name': product.name,
                    'description': product.description,
                    'price': product.price,
                    'price': product.price,
                    'distributor': {
                        'id': product.distributor.id,
                        'name': product.distributor.name,
                        'description': product.distributor.description,
                    },
                    'amount': product.amount,
                    'quantitySold': product.quantitySold,
                }
                return JsonResponse(data)
            else:
                return HttpResponse(status=404)
        
        # Devuelve todos los productos.
        products = list(Products.objects.values())
        data=[]
        print(products)
        for product in products:
            distributor = Distributor.objects.get(id=product['distributor_id'])
            data.append({
                'id': product['id'],
                'name': product['name'],
                'description': product['description'],
                'price': product['price'],
                'distributor': {
                    'id': distributor.id,
                    'name': distributor.name,
                    'description': distributor.description,
                },
                'amount': product['amount'],
                'quantitySold': product['quantitySold'],
            })
        return JsonResponse(data, safe=False)


    def post(self, request):
        jd = js.loads(request.body) # Convertimos el body a json, asi obtenemos los datos.
        Products.objects.create(
            name=jd['name'],
            description=jd['description'],
            price=jd['price'],
            distributor=Distributor.objects.get(id=jd['distributor']),
            amount=jd['amount'],
            quantitySold=jd['quantitySold'],
        )
        data = {'message': 'Success'}
        return JsonResponse(data)

    # Actualiza un producto.
    def put(self, request, id):
        jd = js.loads(request.body)
        if Products.objects.filter(id=id).exists():
                product = Products.objects.get(id=id)
                product.name = jd['name']
                product.description = jd['description']
                product.price = jd['price']
                product.distributor_id = Distributor.objects.get(id=jd['distributor_id'])
                product.amount = jd['amount']
                product.quantitySold = jd['quantitySold']
                product.save()
                data = {'message': 'Success'}
                return JsonResponse(data)
        else:
            return HttpResponse(status=404)

    # Elimina un producto.
    def delete(self, request, id):
        if Products.objects.filter(id=id).exists():
            Products.objects.get(id=id).delete()
            data = {'message': 'Success'}
            return JsonResponse(data)
        else:
            return HttpResponse(status=404)
  

class distributorView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=0):

        # Devuelve distribuidor especifico.
        if id > 0:
            if Distributor.objects.filter(id=id).exists():
                distributor = Distributor.objects.get(id=id)
                data = {
                    'id': distributor.id,
                    'name': distributor.name,
                    'description': distributor.description,
                }
                return JsonResponse(data)
            else:
                return HttpResponse(status=404)
        
        # Devuelve todos los distribuidores.
        distributors = list(Distributor.objects.values())
        data=[]
        for distributor in distributors:
            data.append({
                'id': distributor['id'],
                'name': distributor['name'],
                'description': distributor['description'],
            })
        return JsonResponse(data, safe=False)

    def post(self, request):
        jd = js.loads(request.body) # Convertimos el body a json, asi obtenemos los datos.
        Distributor.objects.create(
            name=jd['name'],
            description=jd['description'],
        )
        data = {'message': 'Success'}
        return JsonResponse(data)

    # Actualiza un distribuidor.
    def put(self, request, id):
        jd = js.loads(request.body)
        if Distributor.objects.filter(id=id).exists():
                distributor = Distributor.objects.get(id=id)
                distributor.name = jd['name']
                distributor.description = jd['description']
                distributor.save()
                data = {'message': 'Success'}
                return JsonResponse(data)
        else:
            return HttpResponse(status=404)

    # Elimina un distribuidor.
    def delete(self, request, id):
        if Distributor.objects.filter(id=id).exists():
            Distributor.objects.get(id=id).delete()
            data = {'message': 'Success'}
            return JsonResponse(data)
        else:
            return HttpResponse(status=404)

    