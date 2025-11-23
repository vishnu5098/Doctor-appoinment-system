from django.shortcuts import render,redirect
from.models import Departments,Doctors,Status
from.forms import BookingForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from.forms import RegisterForms

# Create your views here.
def index(request):

   
    return render(request,'index.html')


  

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            Status.objects.create(booking=booking)
            return render(request, 'confirmation.html')
    else:
        form = BookingForm()  # Only initialize empty form on GET

    return render(request, 'booking.html', {'form': form})

def doctors(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
def status_view(request):
    dict_stat={
        'stat':Status.objects.all()
    }
    return render(request,'status.html',dict_stat)

def contact(request):
    return render(request,'contact.html')

def login_view(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url if next_url else 'booking')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'login.html')

def logout_view(request):
    return render(request,'logout.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = RegisterForms()
    return render(request, 'register.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # ✅ Check if user is linked to a doctor
            if Doctors.objects.filter(user=user).exists():
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                messages.error(request, "This account is not registered as a doctor.")
                return redirect('doctorlogin')

        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'doctorlogin.html')

def doctor_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('doctorlogin')

    # show all bookings with status
    appointments = Status.objects.all()
    return render(request, 'doctor_dashboard.html', {'appointments': appointments})

def approve_booking(request, id):
    status = Status.objects.get(id=id)
    status.status = "Approved"
    status.save()
    return redirect('doctor_dashboard')

def cancel_booking(request, id):
    status = Status.objects.get(id=id)
    status.status = "Cancelled"
    status.save()
    return redirect('doctor_dashboard')

    


