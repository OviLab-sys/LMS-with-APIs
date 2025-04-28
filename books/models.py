from django.db import models

class Subjects(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Subject name

    def __str__(self):
        return self.name


class Books(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name='books')  # Foreign key to Subjects

    def __str__(self):
        return self.title