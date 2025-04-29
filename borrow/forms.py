from django import forms
from .models import Borrowing
from students.models import Student
from books.models import Books

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['student', 'book']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'book': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'student': 'Select Student',
            'book': 'Select Book',
        }