from django.db import models
from books.models import Books

class Student(models.Model):
    student_id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    borrow_limit = models.IntegerField(default=5)
    
    def __str__(self):
        return f"{self.name}: {self.student_id}"
