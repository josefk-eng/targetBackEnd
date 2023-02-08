from django.contrib import admin
from .models import Category,  Season, Banner, Csv, Product, Employee

# Register your models here.
admin.site.register(Category)
admin.site.register(Season)
admin.site.register(Banner)
admin.site.register(Csv)
admin.site.register(Product)
admin.site.register(Employee)
