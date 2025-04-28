from django.db import models
from books.models import Books

class Student(models.Model):
    student_id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    borrow_limit = models.IntegerField(default=5)
    
    def __str__(self):
        return f"{self.name}: {self.student_id}"

class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'student', 'return_date'],
                name='unique_active_borrowing'
            )
        ]
    
    def __str__(self):
        return f"{self.student.name} - {self.book.name} - {self.due_date}"