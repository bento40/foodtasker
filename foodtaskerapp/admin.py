from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import Restaurant

admin.site.register(Restaurant)  #add restaurant in admin panel
