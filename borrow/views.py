from django.shortcuts import render, get_object_or_404,redirect
from .models import Borrowing
from books.models import Books
from students.models import Student
from django.utils.timezone import now
from datetime import timedelta
from django.shortcuts import render
from .models import Borrowing
from .forms import BorrowForm

def borrow_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        borrows = Borrowing.objects.filter(book__title__icontains=query)  # Filter by book title
    else:
        borrows = Borrowing.objects.all()  # Show all borrow records if no query
    context = {'borrows': borrows, 'query': query}
    return render(request, 'borrow/borrow_list.html', context)

def borrow_book(request, student_id, book_id):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')  # Get student_id from the form
        book = get_object_or_404(Books, id=book_id)
        student = get_object_or_404(Student, id=student_id)

        # Check if the book is already borrowed
        if Borrowing.objects.filter(book=book, returned=False).exists():
            return render(request, 'borrow/borrow_error.html', {'message': 'This book is already borrowed.'})

        # Check if the student has reached their borrowing limit
        if Borrowing.objects.filter(student=student, returned=False).count() >= student.borrow_limit:
            return render(request, 'borrow/borrow_error.html', {'message': 'You have reached your borrowing limit.'})

        # Set a due date (e.g., 14 days from now)
        due_date = now().date() + timedelta(days=14)

        # Save the borrow record
        Borrowing.objects.create(student=student, book=book, due_date=due_date)

        return redirect('borrow:borrow_list')
    return redirect('books:book_detail', pk=book_id)

def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrowing, id=borrow_id)  # Ensure a valid borrow record exists
    borrow.is_returned = True
    borrow.return_date = now().date()
    borrow.save()
    return redirect('borrow:borrow_list')