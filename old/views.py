from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import json
from .forms import ProductImageForm
from django.http import JsonResponse
from .utils import *
from django.contrib.auth.models import User , auth
# Create your views here.
def login(request):
    
    if request.method == 'POST':
         username = request.POST['username']
       
         password= request.POST['password']

         user = auth.authenticate(username = username , password = password )
         if user is not None:
             auth.login(request,user)
             return redirect("books")
         else:
             messages.info(request,"User is not found.Please try again!")
             
             return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def logout1(request):
    auth.logout(request)
    return redirect("books")

def signup(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password= request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken")
                return redirect('signup')
                
            elif User.objects.filter(email=email).exists():
                    messages.info(request,"Email is already present")
                    return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=name)
                user.save()
                customer = Customer.objects.create(name=name,email=email,user=user)
                customer.save()
                
                return redirect('login')     
        else:
            messages.info(request,"Passoword is not matching")
            return redirect('signup')
    else:
        return render(request,'signup.html',context)
    
def books(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_cart_item     
    else:
       data = cookieCart(request)
       items = data['items']
       cartItems = data['cartItems']
       cartTotal = data['cartTotal']

    products_details = Product.objects.all()
    context={'products':products_details,'cartItems':cartItems}
    return render(request,'books.html',context)

def store(request):
    return render(request,'store.html')

def books_novel(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_cart_item     
    else:
       data = cookieCart(request)
       items = data['items']
       cartItems = data['cartItems']
       cartTotal = data['cartTotal']
    
    products_details = Product.objects.all().filter(category='Novel')
    context={'products':products_details,'cartItems':cartItems}
    return render(request,'books.html',context)

def books_academics(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_cart_item
	    
    else:
       data = cookieCart(request)
       items = data['items']
       cartItems = data['cartItems']
       cartTotal = data['cartTotal']

    products_details = Product.objects.all().filter(category='Academics')
    context={'products':products_details,'cartItems':cartItems}
    return render(request,'books.html',context)
    

def books_selfHelp(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_cart_item     
    else:       
       data = cookieCart(request)
       items = data['items']
       cartItems = data['cartItems']
       cartTotal = data['cartTotal']

    products_details = Product.objects.all().filter(category='Self help')
    context={'products':products_details,'cartItems':cartItems}
    return render(request,'books.html',context)




def updateCity(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_cart_item
    
    else:
        try:
           cart = json.loads(request.COOKIES['cart'])
        except:
           cart = {}
        order = {'get_cart_total':0,'get_cart_items':0}

        for i in cart:
                order['get_cart_items'] += cart[i]['quantity']
                
                    
        cartItems=order['get_cart_items']
        print('cart:',cart)
        print(cartItems)
    try:
        if request.method == 'POST':
            name = request.POST['search']
            name = name.lower()
            city_name = name[0].upper()+name[1:]
            sellerId = Seller.objects.filter(city=city_name).values_list('id',flat=True)
            print(sellerId)
            products  = Product.objects.all()
            products_details = []
                
            for product in products:
                
                if product.seller.id in sellerId:

                    item = {
                        'id':product.id,
                        'product_name':product.product_name,
                        'price':product.price,
                        'author':product.author,
                        'imageURL':product.imageURL,
                        'seller':{
                            'id':product.seller.id,
                            'seller_name':product.seller.seller_name,
                            'city':product.seller.city
                            },
                        }
                    products_details.append(item)
          
            if len(products_details) > 0:
                context={'products':products_details,'cartItems':cartItems}
                return render(request,'books.html',context)
            else:
                messages.info(request,'Sorry! Unable to find anything.Try with some other name')
                return redirect('books')
    except:
        return redirect('books')
    
   
def updateCart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    sellerId = data['sellerId']

    print('Action',action)
    print('Product ID',productId)
    print('sellerId',sellerId)

    customer = request.user.customer

    product = Product.objects.get(id=productId)
    seller = Seller.objects.get(id=sellerId)
    order, create = Order.objects.get_or_create(customer=customer)
    orderitem , create = OrderItem.objects.get_or_create(order=order,product=product,seller=seller)

    orderitem.save()

    
    if action == 'remove':
        orderitem.quantity -=1

    if orderitem.quantity <= 0:
        orderitem.delete()
   
    return JsonResponse('from server',safe=False)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        try:
            order , created = Order.objects.get_or_create(customer=customer,complete=False)
            items = order.orderitem_set.all() 
            cartItems = order.get_total_cart_item
            cartTotal = order.get_total_cart_price
        except:
           order = {}
           cartItems = 0
           cartTotal = 0
           

    else: 
       data = cookieCart(request)
       items = data['items']
       cartItems = data['cartItems']
       cartTotal = data['cartTotal']

    context={'items': items,'cartItems':cartItems,'cartTotal':cartTotal}
    return render(request,'cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order , created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_total_cart_item
        cartTotal = order.get_total_cart_price
    else: 
       data = cookieCart(request)
       items = data['items']
       cartItems = data['cartItems']
       cartTotal = data['cartTotal']

    context={'items': items,'cartItems':cartItems,'cartTotal':cartTotal}
    return render(request,'checkout.html',context)

def seller(request):
    
    form = ProductImageForm()
    if request.user.is_authenticated:
        
        
        if request.method == 'POST':
            full_name=request.POST['full_name']
            phone_no=request.POST['phone_no']
            email=request.POST['email']
            city=request.POST['city']
            city1 = city[0].upper() + city[1:].lower()
             
            user_id = request.user.id
            seller = Seller.objects.create(seller_name=full_name,user_id=user_id,phone=phone_no,email=email,city=city1)
            seller.save()
            form = ProductImageForm(request.POST , request.FILES)
            if form.is_valid(): 
                form.save()
            user = request.user
            product = Product.objects.filter(seller=None).update(seller=seller)
            messages.info(request,'Books is added successfully')
            return redirect('books')
            
        
        seller_user_id = request.user.id
        sellerId = Seller.objects.filter(user_id = seller_user_id ).values_list('id',flat=True)
        products  = Product.objects.all()
        products_details = []
                
        for product in products:
                
            if product.seller.id in sellerId:

                item = {
                    'id':product.id,
                    'product_name':product.product_name,
                    'price':product.price,
                    'author':product.author,
                    'imageURL':product.imageURL,
                    'seller':{
                        'id':product.seller.id,
                        'seller_name':product.seller.seller_name,
                        'city':product.seller.city
                        },
                    }
                products_details.append(item)
        if len(products_details) > 0:
                
                context={'products':products_details,'form':form}
                return render(request,'seller.html',context)
        else:
                messages.info(request,'Sorry! You did not added any book')
                return render(request,'seller.html',{'form':form})
       
    else:
        return render(request,'seller.html',{'form':form})


def updateSeller(request):
    data =  json.loads(request.body)
    product_id = data['productId']
    seller_id = data['sellerId']
    product = Product.objects.get(id=product_id)
    product.delete()
    seller = Seller.objects.get(id=seller_id)
    seller.delete()
    return JsonResponse("HEllo",safe=False)

    
    
    



    

