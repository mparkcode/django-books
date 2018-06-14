from django import forms
from .models import Book

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','author','isbn','notes','image']