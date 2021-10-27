from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario, ProductoComprado, Venta
import json as js
# Create your views here.

class UserView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    #metodo get
    def get(self, request, id=0):
        # Devuelve un usuario
        if id > 0:
            if Usuario.objects.filter(id=id).exists():
                usuario = Usuario.objects.get(id=id)
                data = {
                    'id': usuario.id,
                    'user': usuario.user,
                    'email': usuario.email,
                    'password': usuario.password,
                    'name': usuario.name,
                    'lastName': usuario.lastName,
                    'address': usuario.address,
                    'phone': usuario.phone,
                    'isAdmin': usuario.isAdmin,
                }
                return JsonResponse(data)
            else:
                return HttpResponse(status=404)
        
        # Devuelve todos los usuarios
        usuarios = list(Usuario.objects.values())
        data=[]
        for usuario in usuarios:
            data.append({
                'id': usuario['id'],
                'user': usuario['user'],
                'email': usuario['email'],
                'password': usuario['password'],
                'name': usuario['name'],
                'lastName': usuario['lastName'],
                'address': usuario['address'],
                'phone': usuario['phone'],
                'isAdmin': usuario['isAdmin'],
            })
        return JsonResponse(data, safe=False)

    #metodo post
    def post(self, request):
        # Crea un usuario
        data = js.loads(request.body)
        usuario = Usuario(
            user=data['user'],
            email=data['email'],
            password=data['password'],
            name=data['name'],
            lastName=data['lastName'],
            address=data['address'],
            phone=data['phone'],
            isAdmin=data['isAdmin'],
        )
        usuario.save()
        return JsonResponse({'message': "Success"})

    #metodo put
    def put(self, request, id):
        # Actualiza un usuario
        data = js.loads(request.body)
        if Usuario.objects.filter(id=id).exists():
            usuario = Usuario.objects.get(id=id)
            usuario.user = data['user']
            usuario.email = data['email']
            usuario.password = data['password']
            usuario.name = data['name']
            usuario.lastName = data['lastName']
            usuario.address = data['address']
            usuario.phone = data['phone']
            usuario.isAdmin = data['isAdmin']
            usuario.save()
            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)

    #metodo delete
    def delete(self, request, id):
        # Elimina un usuario
        if Usuario.objects.filter(id=id).exists():
            Usuario.objects.get(id=id).delete()
            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)


class ProductoCompradoView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #metodo get
    def get(self, request, id=0):
        # Devuelve un producto comprado
        if id > 0:
            if ProductoComprado.objects.filter(id=id).exists():
                productoComprado = ProductoComprado.objects.get(id=id)
                data = {
                    'id': productoComprado.id,
                    'name': productoComprado.name,
                    'description': productoComprado.description,
                    'idOriginalProduct': productoComprado.idOriginalProduct,
                    'salePrice': productoComprado.salePrice,
                    'quantity': productoComprado.quantity,
                }
                return JsonResponse(data)
            else:
                return HttpResponse(status=404)
        
        # Devuelve todos los productos comprados
        productosComprados = list(ProductoComprado.objects.values())
        data=[]
        for productoComprado in productosComprados:
            data.append({
                'id': productoComprado['id'],
                'name': productoComprado['name'],
                'description': productoComprado['description'],
                'idOriginalProduct': productoComprado['idOriginalProduct'],
                'salePrice': productoComprado['salePrice'],
                'quantity': productoComprado['quantity'],
            })
        return JsonResponse(data, safe=False)

    #metodo post
    def post(self, request):
        # Crea un producto comprado
        data = js.loads(request.body)
        productoComprado = ProductoComprado(
            name=data['name'],
            description=data['description'],
            idOriginalProduct=data['idOriginalProduct'],
            salePrice=data['salePrice'],
            quantity=data['quantity'],
        )
        productoComprado.save()
        return JsonResponse({'message': "Success"})

    #metodo put
    def put(self, request, id):
        # Actualiza un producto comprado
        data = js.loads(request.body)
        if ProductoComprado.objects.filter(id=id).exists():
            productoComprado = ProductoComprado.objects.get(id=id)
            productoComprado.name = data['name']
            productoComprado.description = data['description']
            productoComprado.idOriginalProduct = data['idOriginalProduct']
            productoComprado.salePrice = data['salePrice']
            productoComprado.quantity = data['quantity']
            productoComprado.save()
            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)

    #metodo delete
    def delete(self, request, id):
        # Elimina un producto comprado
        if ProductoComprado.objects.filter(id=id).exists():
            ProductoComprado.objects.get(id=id).delete()
            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)


class VentaView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    #metodo get
    def get(self, request, id=0):

        # Devuelve todas las ventas
        ventas = list(Venta.objects.values())
        productList = ProductoComprado.objects.first()
        objects = ProductoComprado.objects.all()
        data=[]
        for venta in ventas:
            user = Usuario.objects.get(id=venta['user_id'])
            data.append({
                'id': venta['id'],
                'user': {
                    'id': user.id,
                    'user': user.user,
                    'email': user.email,
                    'name': user.name,
                    'lastName': user.lastName,
                },
                'sellDate': venta['sellDate'],
                'totalSellPrice': venta['totalSellPrice'],
            })
        return JsonResponse(data, safe=False)
