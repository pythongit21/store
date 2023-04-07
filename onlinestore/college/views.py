from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Department, Course, Purpose, Material, Order, Order_material


# Create your views here.
def index(request):
    return render(request, "home.html")

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("logged in")
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        user_password = request.POST['password']
        confirm = request.POST['confirm']
        if user_password == confirm:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username, password=user_password)
                new_user.save()
                print("registration successful")
                return redirect("login")

        else:
            messages.warning(request, "Password Mismatched")
            return redirect('register')

    return render(request, "register.html")

@login_required
def order(request):
    departments = Department.objects.all()
    purpose = Purpose.objects.all()
    material = Material.objects.all()
    context = {
        'departments': departments,
        'purpose': purpose,
        'material': material
    }
    if request.method == 'POST':
        student = request.POST.get('student')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        purpose_id = request.POST.get('purpose')
        purpose = Purpose.objects.get(id=purpose_id)
        material_list = request.POST.getlist('material')
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        new_order = Order(name=student, dob=dob, age=age, gender=gender, mobile=mobile, email=email, address=address, course=course, purpose=purpose, user=user)
        new_order.save()
        last_id = new_order.id
        print(last_id)
        print(purpose)
        if last_id:
            order_instance = Order.objects.get(id=last_id)
            for item in material_list:
                material_instance = Material.objects.get(id=item)
                order_material = Order_material(order=order_instance, material=material_instance)
                order_material.save()
            messages.info(request, "Your request for "+str(purpose)+" is submitted successfully")
    return render(request, "order.html", context)

def get_courses(request):
    # Get department ID from AJAX request
    department_id = request.GET.get('department_id')
    # Fetch all courses for selected department from database
    courses = Course.objects.filter(department_id=department_id)
    # Create JSON response
    course_list = [{'id': course.id, 'name': course.name} for course in courses]
    response_data = {'courses': course_list}
    return JsonResponse(response_data)
    # return department_id

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def request_view(request):
    # Get the logged in user object
    user = request.user.id

    print(user)

    # Use the user id in your logic
    user_orders = Order.objects.filter(user=user)
    # print(user_orders.user_id)

    # user_order_materials = Order_material.objects.filter(order=user_orders)

    return render(request, 'requests.html', {'user_orders': user_orders})
