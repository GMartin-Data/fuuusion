from django import forms 

from .models import CryptoApi, FlowerFeatures


class CryptoApiForm(forms.ModelForm):
    class Meta:
        model = CryptoApi
        fields = "__all__"
        labels = {
            "slug": "Entrez votre crypto ici",
            "convert": "Entrez votre devise ici"
        }

class FlowerFeaturesForm(forms.ModelForm):
    class Meta:
        model = FlowerFeatures
        fields = "__all__"
        labels = {
            "sepal length": "",
            "sepal width": "",
            "petallength": "",
            "petal width": ""
        }
