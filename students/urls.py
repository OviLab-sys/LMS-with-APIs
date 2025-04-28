from django.urls import path
from . import views 

app_name = 'students'  # Define the app name for namespacing

urlpatterns = [
    path("", views.student_list, name='student_list'),
    path('<int:pk>/', views.student_detail, name='student_detail'),
    path('create/', views.student_create, name='student_create'),
    path('<int:pk>/update', views.student_update, name='student_update'),
    path('<int:pk>/delete/', views.student_delete, name='student_delete'),
]