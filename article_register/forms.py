from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('name','description','entrees','sorties')
        labels = {
            'name':'Name',
            'description':'Description',
            'entrees':'Entrees',
            'sorties':'Sorties'
        }