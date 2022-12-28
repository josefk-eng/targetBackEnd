from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('categories',views.categories,name='categories'),
    path('reports',views.reports,name="reports"),
    path('newCategory', views.addCategory,name='newCat'),
    path('deleteCategory/<id>/', views.deleteCategory,name='deleteCategory'),
    path('deleteItem/<id>/', views.deleteItem,name='deleteItem'),
    path('newItem', views.addItem,name='newItem'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout')
]
