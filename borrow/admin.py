from django.contrib import admin
from django.contrib import admin
from .models import Borrowing  # Import all models from models.py

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    pass