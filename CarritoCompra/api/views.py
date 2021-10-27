from django.http.response import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import CarroscompraProductlist, Usuario, ProductoComprado, Venta, VentaProductlist, carrosCompra
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
    
        # Devuelve una venta
        if id > 0:
            if Venta.objects.filter(id=id).exists():
                venta = Venta.objects.get(id=id)
                productList = list(VentaProductlist.objects.filter(venta_id=venta.id).values())
                products = []

                for i in range(len(productList)):
                    product = list(ProductoComprado.objects.filter(id=productList[i]['productoComprado_id']).values())
                    products.append({
                        'id': product[0]['id'],
                        'name': product[0]['name'],
                        'description': product[0]['description'],
                        'idOriginalProduct': product[0]['idOriginalProduct'],
                        'salePrice': product[0]['salePrice'],
                        'quantity': product[0]['quantity'],
                    })

                data = {
                    'id': venta.id,
                    'user': {
                        'id': venta.user.id,
                        'user': venta.user.user,
                        'email': venta.user.email,
                        'name': venta.user.name,
                        'lastName': venta.user.lastName,
                    },
                    'products': products,
                    'sellDate': venta.sellDate,
                    'totalSellPrice': venta.totalSellPrice,
                }
                return JsonResponse(data)
            else:
                return HttpResponse(status=404)



        # Devuelve todas las ventas
        ventas = list(Venta.objects.values())
        productList = ProductoComprado.objects.first()
        data=[]
        for venta in ventas:
            user = Usuario.objects.get(id=venta['user_id'])
            productList = list(VentaProductlist.objects.filter(venta_id=venta['id']).values())
            products = []

            for i in range(len(productList)):
                product = list(ProductoComprado.objects.filter(id=productList[i]['productoComprado_id']).values())
                products.append({
                    'id': product[0]['id'],
                    'name': product[0]['name'],
                    'description': product[0]['description'],
                    'idOriginalProduct': product[0]['idOriginalProduct'],
                    'salePrice': product[0]['salePrice'],
                    'quantity': product[0]['quantity'],
                })
            
            data.append({
                'id': venta['id'],
                'user': {
                    'id': user.id,
                    'user': user.user,
                    'email': user.email,
                    'name': user.name,
                    'lastName': user.lastName,
                },
                'products': products,
                'sellDate': venta['sellDate'],
                'totalSellPrice': venta['totalSellPrice'],
            })
        return JsonResponse(data, safe=False)



    #metodo post
    def post(self, request):
        # Crea una venta
        jd = js.loads(request.body)
        product = jd['products_id']
        products = []
        for i in product:
            products.append(ProductoComprado.objects.get(id=i))

        venta = Venta(
            user_id= jd['user_id'],
            totalSellPrice=jd['totalSellPrice'],
        )
        venta.save()
        venta.ProductList.set(products)
        return JsonResponse({'message': "Success"})


    #metodo put
    def put(self, request, id):
        # Actualiza una venta
        jd = js.loads(request.body)
        product = jd['products_id']
        products = []
        for i in product:
            products.append(ProductoComprado.objects.get(id=i))
        if Venta.objects.filter(id=id).exists():
            venta = Venta.objects.get(id=id)
            venta.user_id = jd['user_id']
            venta.totalSellPrice = jd['totalSellPrice']
            venta.save()
            venta.ProductList.set(products)

            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)

    #metodo delete
    def delete(self, request, id):
        # Elimina una venta
        if Venta.objects.filter(id=id).exists():
            Venta.objects.get(id=id).delete()
            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)


class carrosCompraView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #metodo get
    def get(self, request, id=0):
        # Devuelve un carro de compra
        if id > 0:
            if carrosCompra.objects.filter(id=id).exists():
                carroCompra = carrosCompra.objects.get(id=id)
                productList = list(CarroscompraProductlist.objects.filter(carrosCompra_id=carroCompra.id).values())
                products = []

                for i in range(len(productList)):
                    product = list(ProductoComprado.objects.filter(id=productList[i]['productoComprado_id']).values())
                    products.append({
                        'id': product[0]['id'],
                        'name': product[0]['name'],
                        'description': product[0]['description'],
                        'salePrice': product[0]['salePrice'],
                        'quantity': product[0]['quantity'],
                    })

                data = {
                    'id': carroCompra.id,
                    'user': {
                        'id': carroCompra.user.id,
                        'user': carroCompra.user.user,
                        'email': carroCompra.user.email,
                        'name': carroCompra.user.name,
                        'lastName': carroCompra.user.lastName,
                    },
                    'products': products,
                    'totalPrice': carroCompra.totalPrice,
                }
                return JsonResponse(data)
            else:
                return HttpResponse(status=404)




        # Devuelve todos los carros de compra
        carros = list(carrosCompra.objects.values())
        data=[]
        for carro in carros:
            user = Usuario.objects.get(id=carro['user_id'])
            productList = list(CarroscompraProductlist.objects.filter(carrosCompra_id=carro['id']).values())
            products = []

            for i in range(len(productList)):
                    product = list(ProductoComprado.objects.filter(id=productList[i]['productoComprado_id']).values())
                    products.append({
                        'id': product[0]['id'],
                        'name': product[0]['name'],
                        'description': product[0]['description'],
                        'salePrice': product[0]['salePrice'],
                        'quantity': product[0]['quantity'],
                    })
            
            data.append({
                'id': carro['id'],
                'user': {
                    'id': user.id,
                    'user': user.user,
                    'email': user.email,
                    'name': user.name,
                    'lastName': user.lastName,
                },
                'products': products,
                'totalPrice': carro['totalPrice'],
            })
        return JsonResponse(data, safe=False)



    #metodo post
    def post(self, request):
        # Crea un carro de compra
        jd = js.loads(request.body)
        product = jd['products_id']
        products = []
        totalPrice = 0
        quantity = 0
        for i in product:
            products.append(ProductoComprado.objects.get(id=i))
        for i in range(len(products)):
            totalPrice += products[i].salePrice * products[i].quantity
            quantity += products[i].quantity

        carro = carrosCompra(
            user_id= jd['user_id'],
            totalPrice=totalPrice,
            quantity=quantity,
        )
        carro.save()
        carro.ProductList.set(products)
        return JsonResponse({'message': "Success"})


    #metodo put
    def put(self, request, id):
        # Actualiza un carro de compra
        jd = js.loads(request.body)
        product = jd['products_id']
        products = []
        totalPrice = 0
        quantity = 0

        for i in product:
            products.append(ProductoComprado.objects.get(id=i))
        for i in range(len(products)):
            totalPrice += products[i].salePrice * products[i].quantity
            quantity += products[i].quantity

        if carrosCompra.objects.filter(id=id).exists():
            carro = carrosCompra.objects.get(id=id)
            carro.user_id = jd['user_id']
            carro.totalPrice = totalPrice
            carro.quantity = quantity
            carro.save()
            carro.ProductList.set(products)

            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)

    #metodo delete
    def delete(self, request, id):
        # Elimina un carro de compra
        if carrosCompra.objects.filter(id=id).exists():
            carrosCompra.objects.get(id=id).delete()
            return JsonResponse({'message': "Success"})
        else:
            return HttpResponse(status=404)