from django.shortcuts import render, get_object_or_404, redirect
from .models import Books,  Subjects
from django.views.decorators.csrf import csrf_exempt
from borrow.forms import BorrowForm

def book_list(request):
    # Fetch all books first
    books = Books.objects.all()

    # Optionally filter books if a search query is provided
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        books = books.filter(title__icontains=query)  # Filter books by title

    # Pass the books and query to the template
    context = {'books': books, 'query': query}
    return render(request, 'books/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    student_id = request.user.student.id if hasattr(request.user, 'student') else None  # Get student_id if logged-in user is a student
    form = BorrowForm(initial={'student': student_id, 'book': book.id})  # Pre-fill the form
    context = {'book': book, 'student_id': student_id, 'form': form}
    return render(request, 'books/book_detail.html', context)

@csrf_exempt
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')
        subject_id = request.POST.get('subject')
        subject = get_object_or_404(Subjects, id=subject_id)
        book = Books.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn,
            subject=subject
        )
        return redirect('books:book_list')
    subjects = Subjects.objects.all()
    return render(request, 'books/book_form.html', {'subjects': subjects})

@csrf_exempt
def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.published_date = request.POST.get('published_date', book.published_date)
        book.isbn = request.POST.get('isbn', book.isbn)
        subject_id = request.POST.get('subject', book.subject.id)
        book.subject = get_object_or_404(Subjects, id=subject_id)
        book.save()
        return redirect('books:book_detail', pk=book.id)
    subjects = Subjects.objects.all()
    return render(request, 'books/book_form.html', {'book': book, 'subjects': subjects})

@csrf_exempt
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    context = {
        'book':book
    }
    return render(request, 'books/book_confirm_delete.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Books,pk=pk)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)

@csrf_exempt
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')
        subject_id = request.POST.get('subject')
        subject = get_object_or_404(Subjects, id=subject_id)
        book = Books.objects.create(
            title=title,
            author=author,
            published_date=published_date,
            isbn=isbn,
            subject=subject
        )
        return redirect('books:book_list')
    subjects = Subjects.objects.all()
    return render(request, 'books/book_form.html', {'subjects': subjects})

@csrf_exempt
def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.published_date = request.POST.get('published_date', book.published_date)
        book.isbn = request.POST.get('isbn', book.isbn)
        subject_id = request.POST.get('subject', book.subject.id)
        book.subject = get_object_or_404(Subjects, id=subject_id)
        book.save()
        return redirect('books:book_detail', pk=book.id)
    subjects = Subjects.objects.all()
    return render(request, 'books/book_form.html', {'book': book, 'subjects': subjects})

@csrf_exempt
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    context = {
        'book':book
    }
    return render(request, 'books/book_confirm_delete.html', context)