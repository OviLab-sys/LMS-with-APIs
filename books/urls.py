from django.urls import path
from . import views

app_name = 'books' 

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Updated name to match the template
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('create/', views.book_create, name='book_create'),
    path('<int:pk>/update/', views.book_update, name='book_update'),
]