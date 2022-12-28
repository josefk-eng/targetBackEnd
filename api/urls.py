from django.urls import path
from . import views

urlpatterns = [
    path('',views.allCategories,name='categories'),
    path('products/<catID>/',views.productsByCatID,name='productsByCatID'),
    path('product/<id>/',views.productsByID,name='productsByID'),
]
