from django.contrib import admin
from shoppingcart.models import Product,Category,Order,OrderDetail,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Contact)

