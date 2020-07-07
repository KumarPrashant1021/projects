from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Seller(models.Model):
    seller_name=  models.CharField(max_length=200,null=True)
    user_id = models.IntegerField(null=True)
    phone =models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)   
    city = models.CharField(max_length=200,null=True) 
    def __str__(self):
        return str(self.id)

    

   

class Product(models.Model):
    seller= models.ForeignKey(Seller,on_delete=models.SET_NULL,blank=True,null=True)
    product_name = models.CharField(max_length=200,blank=True,null=True)
    author= models.CharField(max_length=200,null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    category = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to ="pics/",null=True,blank=True)

    def __str__(self):
       
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url



class Order(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_cart_price(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_total_cart_item(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems ])
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True,null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, blank=True,null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price
        return total
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    pincode = models.IntegerField(null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



    
