from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant, Customer, Driver, Meal, Order, OrderDetails

admin.site.register(Restaurant)  #add restaurant in admin panel
admin.site.register(Customer)  #add customer in admin panel
admin.site.register(Driver)  #add Driver in admin panel
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(OrderDetails)
