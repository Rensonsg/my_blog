from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']
        widgets ={ 'fecha_publicacion':forms.DateInput(attrs={'type':'date'}),}