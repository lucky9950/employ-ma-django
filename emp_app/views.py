from django.shortcuts import render,HttpResponse
from emp_app.models import Department,Role,Employee
from datetime import datetime

# Create your views here.


def index(request):
    return render(request,'index.html')

def view_all_emp(request):
    
    emps = Employee.objects.all()
    
    context = {
        'emps' : emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role = request.POST['role']
        dept = request.POST['dept']
        hire_date = request.POST['hire_date']

        
        # new_emp = Employee(first_name = first_name,last_name = last_name,salary = salary,bonus = bonus,phone = phone,role = role,dept = dept,hire_date = datetime.now())
        
        # new_emp.save()
        
        add_emp = Employee(first_name = first_name, last_name = last_name, dept = dept, salary = salary, bonus = bonus, role = role, phone = phone, hire_date = datetime.now())
        
        add_emp.save()
        
        return HttpResponse("employee added succesfully...")
    
    elif request.method=='GET':
        return render(request,'add_emp.html')
    
    else:
        return HttpResponse("An Exception occur...")

def remove_emp(request):
    return render(request,'remove_emp.html')


def filter_emp(request):
    return render(request,'filter_emp.html')