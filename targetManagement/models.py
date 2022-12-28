from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, default="")
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True,upload_to="img/cats")
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='img/items')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Item_detail", kwargs={"pk": self.pk})

