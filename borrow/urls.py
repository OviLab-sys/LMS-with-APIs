from django.urls import path
from . import views

app_name = 'borrow'

urlpatterns = [
    path('', views.borrow_list, name='borrow_list'),
    path('<int:student_id>/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('return/<int:borrow_id>/', views.return_book, name='return_book'),
]