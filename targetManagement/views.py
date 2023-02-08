from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.http import JsonResponse
from django.template.loader import render_to_string

from api import FCMManager
from .form import ItemForm, CatForm, BannerForm, SeasonForm, CsvForm
from .models import Category, Banner, Season, Csv, Employee, Product
import csv
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        items = Product.objects.all()
        categories = Category.objects.all()
        form = ItemForm()
        csvForm = CsvForm()
        return render(request, 'items.html',
                      {'products': items, 'categories': categories, 'form': form, 'csvform': csvForm})
    else:
        return redirect('login')


def categories(request, id):
    if request.user.is_authenticated:
        category = get_object_or_404(Category, id=id)
        items = Product.objects.filter(category=category)
        form = CatForm()
        return render(request, 'testfile.html', {'products': items, 'category': category, 'form': form})
    else:
        return redirect('login')


def banners(request):
    if request.user.is_authenticated:
        allBanners = Banner.objects.all()
        form = BannerForm()
        id = -1
        return render(request, 'Banners.html', {'banners': allBanners, 'form': form, "id": id})
    else:
        return redirect('login')


def editBanner(request, id):
    if request.user.is_authenticated:
        banner = get_object_or_404(Banner, id=id)
        allBanners = Banner.objects.all()
        form = BannerForm(instance=banner)
        id = id
        return render(request, 'Banners.html', {'banners': allBanners, 'form': form, "id": id})
    else:
        return redirect('login')


def newBanner(request, id):
    if request.method == 'POST':
        banner = None
        if id != "-1":
            banner = get_object_or_404(Banner, id=id)
        bannerForm = BannerForm(data=request.POST, files=request.FILES, instance=banner)
        if bannerForm.is_valid():
            bannerForm.save()
            banner = Banner.objects.filter(header=request.POST['header']).order_by('-id')[0]
            FCMManager.sendpush("Banner", "{}".format(banner.id))
            messages.success(request, "Banner {} has been added successfully".format(request.POST['header']))
            return redirect('banners')
        else:
            messages.error(request,
                           "Could Not Save Banner {} due to {}".format(request.POST['header'], bannerForm.errors))
            return redirect('banners')
    else:
        messages.error(request, "Not a Valid POST")
        return render(request, 'Banners.html')


def seasons(request):
    if request.user.is_authenticated:
        allSeasons = Season.objects.all()
        form = SeasonForm()
        return render(request, 'Seasons.html', {'seasons': allSeasons, 'form': form})
    else:
        return redirect('login')


def newSeason(request):
    if request.method == 'POST':
        seasonForm = SeasonForm(request.POST)
        if seasonForm.is_valid():
            seasonForm.save()
            # season = Season.objects.filter(name=request.POST['name']).order_by('-id')[0]
            # FCMManager.sendpush("Category", "{}".format(category.id))
            messages.success(request, "Season {} has been added successfully".format(request.POST['name']))
            return redirect('seasons')
        else:
            messages.error(request,
                           "Could Not Save Season {} due to {}".format(request.POST['name'], seasonForm.errors))
            return redirect('seasons')
    else:
        messages.error(request, "Not a Valid POST")
        return render(request, 'Seasons.html')


def deleteCategory(request, id):
    Category.objects.filter(id=id).delete()
    return redirect('categories')


def deleteItem(request, id):
    Product.objects.filter(id=id).delete()
    return redirect('index')


def deleteSeason(request, id):
    Season.objects.filter(id=id).delete()
    return redirect('seasons')


def deleteBanner(request, id):
    Banner.objects.filter(id=id).delete()
    FCMManager.sendpush("Banner_d", "{}".format(id))
    return redirect('banners')


def reports(request):
    if request.user.is_authenticated:
        return render(request, 'reports.html')
    else:
        return redirect('login')


def addCategory(request):
    if request.method == 'POST':
        catForm = CatForm(request.POST, request.FILES)
        if catForm.is_valid():
            catForm.save()
            category = Category.objects.filter(name=request.POST['name']).order_by('-id')[0]
            FCMManager.sendpush("Category", "{}".format(category.id))
            messages.success(request, "Category {} has been added successfully".format(request.POST['name']))
            return redirect('categories')
        else:
            messages.error(request, "Could Not Save category {} due to {}".format(request.POST['name'], catForm.errors))
            return redirect('categories')
    else:
        messages.error(request, "Not a Valid POST")
        return render(request, 'categories.html')


def addItem(request):
    if request.method == 'POST':
        imgForm = ItemForm(request.POST, request.FILES)
        if imgForm.is_valid():
            imgForm.save()
            item = Product.objects.filter(name=request.POST['name']).order_by('-id')[0]
            FCMManager.sendpush("Item", "{}".format(item.id))
            messages.success(request, "Item {} has been added successdully".format(request.POST['name']))
            return redirect('index')
        else:
            messages.error(request, "Could Not Save item {} due to {}".format(request.POST['name'], imgForm.errors))
            return redirect('index')
    else:
        messages.error(request, "Not a Valid POST")
        return render(request, 'index.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Wrong credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return redirect('login')


def uploadcsv(request):
    csvForm = CsvForm(request.POST or None, request.FILES or None)
    items = Product.objects.all()
    categories = Category.objects.all()
    user = request.user
    form = ItemForm()
    if csvForm.is_valid():
        csvForm.save()
        csvForm = CsvForm()
        obj = Csv.objects.get(is_activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    number = row[0]
                    stock_id = row[1]
                    tmp = row[2]
                    try:
                        serial_number = float(tmp)
                    except:
                        serial_number = 0
                    name = row[3].upper()
                    quantity = row[4]
                    cost_price = row[5]
                    price = row[6]
                    cat, created = Category.objects.get_or_create(
                        name=row[8]
                    )
                    department = Employee.objects.get(id=user.id).department
                    availability = quantity != "0"
                    Product.objects.create(
                        number=number,
                        stockId=stock_id,
                        serialNumber=serial_number,
                        name=name,
                        quantity=quantity,
                        cost_price=cost_price,
                        price=price,
                        department=department,
                        category=cat,
                        availability=availability
                    )
                    # print(row)
                    # print(type(row))
            obj.is_activated = True
            obj.save()
    return render(request, 'items.html',
                  {'products': items, 'categories': categories, 'form': form, 'csvform': csvForm})


def addNewCategory(name):
    Category.objects.create(
        name=name
    )
    return Category.objects.filter(name=name).first


def toggle_visibility(request, prod_id, route):
    try:
        prod = Product.objects.get(id=prod_id)
        prod.availability = not prod.availability
        prod.save()
        FCMManager.sendpush("item", "{}".format(prod_id))
    except Product.DoesNotExist:
        print("failed.........................")
    return redirect(route)


def toggle_cat_visibility(request, cat_id, route):
    try:
        prod = Category.objects.get(id=cat_id)
        prod.availability = not prod.availability
        prod.save()
    except Category.DoesNotExist:
        print("failed.........................")
    return redirect(route)


def edit_page(request, id, cat):
    if request.user.is_authenticated:
        category = get_object_or_404(Category, id=cat)
        items = Product.objects.filter(category=category)
        product = get_object_or_404(Product, id=id)
        form = ItemForm(instance=product)
        return render(request, 'testfile.html', {'products': items, 'category': category, 'form': form})
    else:
        return redirect('login')


class BookCreateView(BSModalCreateView):
    template_name = 'create_product.html'
    form_class = ItemForm
    success_message = 'Success: Product was created.'
    success_url = reverse_lazy('index')


def products(request):
    data = dict()
    if request.method == 'GET':
        products = Product.objects.all()
        # asyncSettings.dataKey = 'table'
        data['section'] = render_to_string(
            '_books_table.html',
            {'products': products},
            request=request
        )
        return JsonResponse(data)


class ProductUpdateView(BSModalUpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = ItemForm
    success_message = 'Success: Product was Updated.'
    success_url = reverse_lazy('index')
