from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'write some text...'
        }
    ))

    class Meta:
        model = Post
        fields = [
            'post'
        ]