from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Student

#List all students
def student_list(request):
    students = Student.objects.all()
    context = {
        'students':students
    }
    return render(request, 'students/student_list.html',context)

#Retrieve details of a specific student
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)  # Pass pk as a keyword argument
    context = {'student': student}
    return render(request, 'students/student_detail.html', context)

#create a new 
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        student = Student.objects.create(
            name =name,
            age = age,
            email = email
        )
        return redirect('student_detail', pk = student.id)
    return render(request, 'students/students_form.html')

#Update an existing student
@csrf_exempt
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST.get('name',student.name)
        student.age = request.POST.get('age',student.age)
        student.email = request.POST.get('email',student.email)
        student.save()
        return redirect('student_detail', pk = student.id)
    context = {
        'student': student
    }
    return render(request,'students/student_form.html', context)

#Delete a student
@csrf_exempt
def student_delete(request, pk):
    student = get_object_or_404(Student, pk = pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    context = {
        'student': student
    }
    return render(request, 'students/student_confirm_delete.html',context)