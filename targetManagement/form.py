from django.forms import ModelForm, TextInput, Select, FileInput
from .models import Category, Banner, Season, Csv, Product
from django.shortcuts import get_object_or_404
from bootstrap_modal_forms.forms import BSModalModelForm


class ItemForm(BSModalModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter Name',
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Enter Description',
                }
            ),
            'category': Select(
                attrs={
                    'style': 'width:100%;'
                }
            ),
            'department': TextInput(
                attrs={
                    'placeholder': 'Enter Department',
                }
            ),

        }


class CatForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter Name',
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Enter Description',
                }
            ),
            'season':Select(
                attrs={
                    'style':'width:100%;'
                }
            )
        }


class BannerForm(ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
        enctype = "multipart/form-data"
        ISMAIN = ((True, 'Yes'), (False, 'No'),)
        BUTTONALIGN = (('Center','center'),('Left','left'),('Right','right'))
        widgets = {
            'header': TextInput(
                attrs={
                    'placeholder': 'Enter Header',
                }
            ),
            'caption': TextInput(
                attrs={
                    'placeholder': 'Enter Banner Caption',
                }
            ),
            'season':Select(
                attrs={
                    'style': 'width:100%;'
                }
            ),
            'isMain':Select(
                attrs={
                    'style': 'width:100%;border:none'
                },
                choices=ISMAIN
            ),
            'buttonAlign':Select(
                attrs={
                    'style': 'width:100%;border:none'
                },
                choices=BUTTONALIGN
            )
        }



class SeasonForm(ModelForm):
    class Meta:
        model = Season
        fields = '__all__'
        CHOICES = (('Yes', True), ('No', False),)
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter Season Name',
                }
            ),
            'isActive': Select(
                attrs={
                    'style': 'width:100%;border:none'
                },
                choices=CHOICES
            ),
        }


class CsvForm(ModelForm):
    class Meta:
        model = Csv
        fields = ('file_name',)


class ProductToggleForm(ModelForm):
    class Meta:
        model = Product
        fields = ('availability',)
