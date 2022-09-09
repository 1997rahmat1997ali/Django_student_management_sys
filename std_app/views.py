from django.shortcuts import render, HttpResponse
from .models import Student, Sec, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')


def all_std(request):
    stds = Student.objects.all()
    context = {
        'stds': stds
    }
    print(context)
    return render(request, 'view_all_std.html', context)


def add_std(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        roll_no = int(request.POST['roll_no'])
        dept = int(request.POST['dept'])
        sec = int(request.POST['sec'])
        year = int(request.POST['year'])
        phone = int(request.POST['phone'])
        new_std = Student(first_name= first_name, last_name=last_name, roll_no=roll_no, year=year, phone=phone, dept_id = dept, sec_id = sec, add_date = datetime.now())
        new_std.save()
        return HttpResponse('Student added Successfully')
    elif request.method=='GET':
        return render(request, 'add_std.html')
    else:
        return HttpResponse("An Exception Occured! Student Has Not Been Added")


def remove_std(request, std_id = 0):
    if std_id:
        try:
            std_to_be_removed = Student.objects.get(id=std_id)
            std_to_be_removed.delete()
            return HttpResponse("Student Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid STD ID")
    stds = Student.objects.all()
    context = {
        'stds': stds
    }
    return render(request, 'remove_std.html',context)


def filter_std(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        sec = request.POST['sec']
        stds = Student.objects.all()
        if name:
            stds = stds.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            stds = stds.filter(dept__name__icontains = dept)
        if sec:
            stds = stds.filter(sec__name__icontains = sec)

        context = {
            'stds': stds
        }
        return render(request, 'view_all_std.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_std.html')
    else:
        return HttpResponse('An Exception Occurred')
