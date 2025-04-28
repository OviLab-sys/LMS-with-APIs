from django.shortcuts import render, get_object_or_404,redirect
from .models import Borrowing
from books.models import Books
from students.models import Student
from django.utils.timezone import now

from django.shortcuts import render
from .models import Borrowing

def borrow_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        borrows = Borrowing.objects.filter(book__title__icontains=query)  # Filter by book title
    else:
        borrows = Borrowing.objects.all()  # Show all borrow records if no query
    context = {'borrows': borrows, 'query': query}
    return render(request, 'borrow/borrow_list.html', context)

def borrow_book(request, student_id, book_id):
    student = get_object_or_404(Student, id=student_id)
    book = get_object_or_404(Books, id=book_id)

    # Check if the book is already borrowed
    if Borrowing.objects.filter(book=book, returned=False).exists():
        return render(request, 'borrow/borrow_error.html', {'message': 'This book is already borrowed.'})

    # Create a borrow record
    Borrowing.objects.create(student=student, book=book, due_date=now().date())
    return redirect('books:book_list')

#return a book
def return_book(request, borrow_id):
    borrow=get_object_or_404(Borrowing,id=borrow_id)
    borrow.is_returned=True
    borrow.return_date=now().date()
    borrow.save()
    return redirect('borrow:borrow_list')