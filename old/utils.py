import json
from .models import *

def cookieCart(request):

       try:
           cart = json.loads(request.COOKIES['cart'])
       except:
           cart = {}

       print('Cart:',cart)
       items = []
       order = {'get_cart_total':0,'get_cart_items':0}
       cartItems  = order['get_cart_items']

       for i in cart:
           try:
               cartItems += cart[i]['quantity']

               product = Product.objects.get(id=i)
               total = product.price

               order['get_cart_total'] += total
               order['get_cart_items'] += cart[i]['quantity']

               item={
                   'product':{
                       'id':product.id,
                       'product_name':product.product_name,
                       'price':product.price,
                       'imageURL':product.imageURL,
                       
                       },
                   'seller':{
                       'seller_name':product.seller.seller_name
                       },
                   }
               items.append(item)
           except:
              pass
       
       cartItems = order['get_cart_items']
       cartTotal = order['get_cart_total']

       return {"items":items,"cartItems":cartItems,"cartTotal":cartTotal}