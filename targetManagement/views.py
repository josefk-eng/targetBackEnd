from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Category, Item
from .form import ItemForm, CatForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        items = Item.objects.all()
        categories = Category.objects.all()
        form = ItemForm()
        return render(request,'items.html',{'products':items,'categories':categories,'form':form})
    else:
        return redirect('login')
    
def categories(request):
    if request.user.is_authenticated:
        categories = Category.objects.all()
        form = CatForm()
        return render(request,'categories.html',{'categories':categories,'form':form})
    else:
        return redirect('login')
    
def deleteCategory(request, id):
    Category.objects.filter(id=id).delete()
    return redirect('categories')
    
def deleteItem(request, id):
    Item.objects.filter(id=id).delete()
    return redirect('index')
    
def reports(request):
    if request.user.is_authenticated:
        return render(request,'reports.html')
    else:
        return redirect('login')
    
def addCategory(request):
    if request.method == 'POST':
        catForm = CatForm(request.POST, request.FILES)
        if catForm.is_valid():
            catForm.save()
            messages.success(request, "Category {} has been added successfully".format(request.POST['name']))
            return redirect('categories')
        else:
            messages.error(request, "Could Not Save category {} due to {}".format(request.POST['name'], catForm.errors))
            return render(request, 'categories.html')
    else:
        messages.error(request,"Not a Valid POST")
        return render(request, 'categories.html')
        
def addItem(request):
    if request.method == 'POST':
        imgForm = ItemForm(request.POST, request.FILES)
        if imgForm.is_valid():
            imgForm.save()    
            messages.success(request,"Item {} has been added successdully".format(request.POST['name']))
            return redirect('index')
        else:
            messages.error(request, "Could Not Save item {} due to {}".format(request.POST['name'], imgForm.errors))
            return redirect('index')
    else:
        messages.error(request,"Not a Valid POST")
        return render(request,'index.html')
    
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth_logout(request)
    return redirect('login')
    