from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import UserProfile
from .models import User 
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import EmployeeForm
from django.shortcuts import render, get_object_or_404
from .models import University
from .forms import StudentForm
from django.utils.timezone import now
import datetime
from django.http import HttpResponseRedirect
from urllib.parse import urlparse
from django.urls import is_valid_path
#from .models import StudentProfile, EmployeeProfile
#from .forms import StudentProfileForm
from .decorators import unauthenticated_user
#from home import views
from django.http import HttpResponseForbidden
from .decorators import admin_only


def admin_dashboard(request):
    student_count = StudentProfile.objects.count()
    employee_count = EmployeeProfile.objects.count()
    return render(request, 'admin/admin.html', {
        'student_count': student_count,
        'employee_count': employee_count,
    })

'''
def login_view(request):
   if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Initialize login attempts in the session if not present
        if 'login_attempts' not in request.session:
            request.session['login_attempts'] = 0
        
        # Check if the user is temporarily locked out
        if request.session.get('lockout_until'):
            lockout_until = datetime.datetime.strptime(request.session['lockout_until'], '%Y-%m-%d %H:%M:%S')
            if now() < lockout_until:
                messages.error(request, f"Too many failed attempts. Try again after {lockout_until}.")
                return render(request, 'home/login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Reset login attempts on successful login
            request.session['login_attempts'] = 0
            login(request, user)
            return redirect('home')  # Redirect to the home page or a specific URL
        else:
            # Increment login attempts
            request.session['login_attempts'] += 1
            if request.session['login_attempts'] >= 3:
                # Lockout the user for 5 minutes
                lockout_time = now() + datetime.timedelta(minutes=5)
                request.session['lockout_until'] = lockout_time.strftime('%Y-%m-%d %H:%M:%S')
                messages.error(request, "Too many failed attempts. You are locked out for 5 minutes.")
            else:
                messages.error(request, f"Invalid credentials. {3 - request.session['login_attempts']} attempts left.")
                
                return render(request, 'home/login.html') 
'''


def admin_dashboard(request):
    if request.user.is_authenticated and request.user.is_staff:  # Assuming is_staff means admin
        # Load admin-specific data
        admin_data = {'title': 'Admin Dashboard', 'data': 'Admin-only data here'}
        return render(request, 'admin_dashboard.html', admin_data)
    else:
        return HttpResponseForbidden("You are not authorized to view this page.")

'''
def login_view(request):
    next_url = request.GET.get('next', '/')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Ensure next_url is safe or default to home page
            next_url = request.POST.get('next', next_url)
            parsed_url = urlparse(next_url)
            if not parsed_url.netloc and is_valid_path(next_url):
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect('home/welcome.html')
    else:
        form = AuthenticationForm()

    return render(request, 'home/login.html', {'form': form, 'next': next_url})
'''
'''
def custom_logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login/')  # Redirect to login
    return HttpResponse("Logout requires a POST request.", status=405)
'''


#def index(request):
  #  return render(request, 'index.html')

def home(request):
    universities = University.objects.all()
    return render(request,'home/welcome.html')
'''
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect('home')  # Redirect to home after successful login
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'home/login.html', {'form': form})
    #return HttpResponse("Welcome")
    '''

    
def logout_view(request):
    logout(request)
    
    return render(request,'home/login.html',context=None)

def ContactUs(request):
    return HttpResponse("ContactUs")

def reset_password_view(request):
    """
    Handle reset password logic, send an email with reset link.
    """
    if request.method == "POST":
        email = request.POST.get('email')
        
        try:
            user = User.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())
            # Get the domain name
            domain = get_current_site(request).domain
            reset_link = f"http://{domain}/home/password_reset_confirm/{uid}/{token}"

            # Send the email
            subject = "Password Reset Request"
            message = f"Click the link to reset your password: {reset_link}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            
            messages.success(request, "Password reset link has been sent to your email address.")
            return redirect('home/login.html')  # Redirect to login after sending the email
        except User.DoesNotExist:
            messages.error(request, "No account associated with this email.")
    
    return render(request, 'home/password_reset_form.html')

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Replace 'item_list' with the name of your redirect URL
    else:
        form = ItemForm()
    return render(request, 'create_item.html', {'form': form})

# Update Item
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')  # Replace 'item_list' with the name of your redirect URL
    else:
        form = ItemForm(instance=item)
    return render(request, 'update_item.html', {'form': form, 'item': item})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})




def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the employee data to the database
            return redirect('employee_success')  # Redirect to a success page (you can create this page later)
    else:
        form = EmployeeForm()
    
    return render(request, 'home/employee_form.html', {'form': form})

def employee_success(request):
    return render(request, 'home/success.html')

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'home/item_form.html', {'form': form})

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'home/item_form.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'home/confirm_delete.html', {'item': item})

def student_form(request):
    if request.method =='POST':
        form = student_form(request.POST)
        if form.is_valid():
             # Process the form data here (e.g., save to the database)
            # You can access form data via form.cleaned_data
            # student = form.save() # Save to model (if you use a model)
                    return render(request, 'success.html', {'form': form})
    else:
        form = StudentForm()

    return render(request, 'home/student_form.html', {'form': form})    



from .models import StudentProfile, EmployeeProfile
from .forms import StudentProfileForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Admin Restriction
def admin(user):
    return user.is_superuser


'''  

#Admin Dashboard
@login_required
@user_passes_test(isadmin)
def admin_dashboard(request):
    student_count = StudentProfile.objects.count()
    employee_count = EmployeeProfile.objects.count()
    return render(request, 'home/admin.html', {
        'student_count': student_count,
        'employee_count': employee_count,
    })
''' '''
    
# List Students
@login_required
@user_passes_test(is_admin)
def admin_student_list(request):
    students = StudentProfile.objects.all()
    return render(request, 'home/student_list.html', {'students': students})

# Add Student
@login_required
@user_passes_test(is_admin)
def admin_add_student(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_student_list')
    else:
        form = StudentProfileForm()
    return render(request, 'home/add_student.html', {'form': form})

# Update Student
@login_required
@user_passes_test(is_admin)
def admin_update_student(request, pk):
    student = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('admin_student_list')
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'home/update_student.html', {'form': form})

# Delete Student
@login_required
@user_passes_test(is_admin)
def admin_delete_student(request, pk):
    student = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('admin_student_list')
    return render(request, 'home/delete_student.html', {'student': student})


   '''


@admin_only
def admin_dashboard(request):
    # Load admin-specific data
    admin_data = {'title': 'Admin Dashboard', 'data': 'Admin-only data here'}
    return render(request, 'admin_dashboard.html', admin_data)

def admin_dashboard(request):
    # Load admin-specific data
    admin_data = {'title': 'Admin Dashboard', 'data': 'Admin-only data here'}
    return render(request, 'admin_dashboard.html', admin_data)

# views.py (add this to create a home page)
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home/welcome.html')  # Create a home.html template for the logged-in users


import random
import string

@login_required
# Custom login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        captcha_input = request.POST.get('captcha_input')

           # CAPTCHA validation
    if captcha_input != request.session.get('captcha'):
               messages.error(request, "Incorrect CAPTCHA.")
               return redirect('login')  # Reload the login page

        # User authentication
    user = authenticate(request, username=username, password=password)
    if user is not None:
            login(request, user)  # Log the user in
            return redirect('welcome')  # Redirect to a home page after successful login
    else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # Reload the login page

    # Generate CAPTCHA and store it in session
    captcha = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    request.session['captcha'] = captcha

    return render(request, 'home/login.html', {'captcha': captcha})
    
from .forms import ProfileForm
from .models import Profile

def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'home/base_generic.html', {'form': form})