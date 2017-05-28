from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant, Customer, Driver

admin.site.register(Restaurant)  #add restaurant in admin panel
admin.site.register(Customer)  #add customer in admin panel
admin.site.register(Driver)  #add Driver in admin panel
