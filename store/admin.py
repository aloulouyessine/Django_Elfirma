from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Mouton)
admin.site.register(Fruit)
admin.site.register(Vache)
admin.site.register(Laitiers)