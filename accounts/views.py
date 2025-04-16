from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Plant, PlantStatus

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Đăng ký thành công. Vui lòng đăng nhập.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'UI/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Đăng nhập thành công!")
            return redirect('home')
        else:
            messages.error(request, "Thông tin đăng nhập không đúng.")
    else:
        form = LoginForm()
    return render(request, 'UI/login.html', {'form': form})

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Lấy danh sách cây của người dùng hiện tại
    plants = Plant.objects.filter(owner=request.user)
    return render(request, 'UI/home.html', {'plants': plants})

def plant_dashboard(request, plant_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    plant = get_object_or_404(Plant, id=plant_id, owner=request.user)  # Chỉ cho phép xem cây của người dùng
    latest_status = plant.statuses.first()  # Trạng thái mới nhất
    
    context = {
        'plant': plant,
        'latest_status': latest_status,
    }
    return render(request, 'UI/plant_dashboard.html', context)

def plant_history(request, plant_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    plant = get_object_or_404(Plant, id=plant_id, owner=request.user)
    statuses = plant.statuses.all()  # Lấy tất cả trạng thái của cây
    
    context = {
        'plant': plant,
        'statuses': statuses,
    }
    return render(request, 'UI/plant_history.html', context)
