from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName =models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName
 
 
class Product(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=122)
    productCategory = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products",null=True,blank=True)
    productPrice = models.IntegerField(default=0)
    productDescription = models.TextField()
    productImage=models.ImageField(upload_to="shoppingcart/productImages",default="")
    productPublishDate = models.DateField()
    
    def __str__(self):
        return self.productName
    
class Order(models.Model):
    orderId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(User,on_delete=models.CASCADE,related_name="order",null=True,blank=True)
    Address = models.CharField(max_length=500)
    MobileNumber = models.IntegerField(default="")
    totalPrice = models.IntegerField(default=0)
    date=models.DateField()
    def __str__(self):
        return str(self.orderId)
    
class OrderDetail(models.Model):
    orderDetailId = models.AutoField(primary_key=True)
    productId = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="productOrderId",null=True,blank=True)
    orderId = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="orderDetailId",null=True,blank=True)
    orderProductQuantity = models.IntegerField(default=0)
    productPrice = models.IntegerField(default=0)
    def __str__(self):
        return str(self.orderId)
    

class Contact(models.Model):
    contactId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=122)
    Email = models.CharField(max_length=122)
    Subject = models.CharField(max_length=122,null=True,blank=True)
    Message = models.TextField()    
    def __str__(self):
        return str(self.Name)
    