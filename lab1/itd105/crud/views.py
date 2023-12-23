from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import medicine

def login(request):
    return render(request, 'signin.html')

def register(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(username=email, email=email, password=password)
        # Redirect to a success page or any other page
        return render(request, "signin.html")

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)

        
        meds = medicine.objects.all()

        # Extract brand names and their counts
        name_counts = {}
        for med in meds:
            name = med.med_name
            name_counts[name] = name_counts.get(name, 0) + 1

        # Prepare data for the chart
        labels = list(name_counts.keys())
        values = list(name_counts.values())

        status_counts = {}
        for med in meds:
            status = med.med_status
            status_counts[status] = status_counts.get(status, 0) + 1

        # Prepare data for the chart
        stat_labels = list(status_counts.keys())
        stat_values = list(status_counts.values())


        context = {
            'labels': labels,
            'values': values,
            'stat_labels': stat_labels,
            'stat_values': stat_values,
        }

        return render(request, 'index.html', context)
    else:
        # Handle invalid login (display an error message or redirect back to the login page)
        return render(request, 'signin.html', {'error': 'Invalid login credentials'})


def signout(request):
    logout(request)
    return redirect('/')

def index(request):
    # Retrieve all medicine instances
    meds = medicine.objects.all()

    # Extract brand names and their counts
    name_counts = {}
    for med in meds:
        name = med.med_name
        name_counts[name] = name_counts.get(name, 0) + 1

    # Prepare data for the chart
    labels = list(name_counts.keys())
    values = list(name_counts.values())

    status_counts = {}
    for med in meds:
        status = med.med_status
        status_counts[status] = status_counts.get(status, 0) + 1

    # Prepare data for the chart
    stat_labels = list(status_counts.keys())
    stat_values = list(status_counts.values())


    context = {
        'labels': labels,
        'values': values,
        'stat_labels': stat_labels,
        'stat_values': stat_values,
    }

    return render(request, 'index.html', context)

def add_view(request):
    return render (request, "add.html")

def add_med(request):
    if request.method == 'POST':
        # Extract form data from the request
        med_name = request.POST.get('med_name')
        med_brand = request.POST.get('med_brand')
        med_dosage = request.POST.get('med_dosage')
        med_expiry = request.POST.get('med_expiry')
        med_stock = int(request.POST.get('med_stock'))
        med_status = request.POST.get('med_status')

        # Create and save a new instance of YourModelName
        medicine.objects.create(
            med_name=med_name,
            med_brand=med_brand,
            med_dosage=med_dosage,
            med_expiry=med_expiry,
            med_stock=med_stock,
            med_status=med_status
        )

        message = "Data Successfully Added"
        #return redirect(reverse('eda'))
        return redirect("/view")

    return render(request, 'add.html')

def view(request):
    med = medicine.objects.all()
    return render (request, "view.html", {'med':med})

def edit(request, id):  
    med = medicine.objects.get(id=id)  
    return render(request,'edit.html', {'med':med})

def update(request, id):  
    med = medicine.objects.get(id=id)  
    
    if request.method == 'POST':
        # Extract form data from the request
        med_name = request.POST.get('med_name')
        med_brand = request.POST.get('med_brand')
        med_dosage = request.POST.get('med_dosage')
        med_expiry = request.POST.get('med_expiry')
        med_stock = int(request.POST.get('med_stock'))
        med_status = request.POST.get('med_status')

        # Update the existing instance
        med.med_name = med_name
        med.med_brand = med_brand
        med.med_dosage = med_dosage
        med.med_expiry = med_expiry
        med.med_stock = med_stock
        med.med_status = med_status

        # Save the updated instance
        med.save()

        return redirect("/view")

    return render(request, 'edit.html', {'med': med})


def destroy(request, id):  
    med = medicine.objects.get(id=id)  
    med.delete()
    return redirect("/view")  
