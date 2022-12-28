from django.forms import ModelForm, TextInput, Select
from .models import Item, Category

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'name':TextInput(
                attrs={
                    'placeholder':'Enter Name',
                }
            ),
            'description':TextInput(
                attrs={
                    'placeholder':'Enter Description',
                }
            ),
            'category':Select(
                attrs={
                    'style':'width:100%;'
                }
            )
            
        }
        
class CatForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name':TextInput(
                attrs={
                    'placeholder':'Enter Name',
                }
            ),
            'description':TextInput(
                attrs={
                    'placeholder':'Enter Description',
                }
            )
            
        }