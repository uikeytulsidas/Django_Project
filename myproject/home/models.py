from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django import forms

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.username
    
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
  


class Employee(models.Model):
    # Name fields
    FIRST_NAME = models.CharField(max_length=30, null=False)
    MIDDLE_NAME = models.CharField(max_length=30, null=False)
    LAST_NAME = models.CharField(max_length=30, null=False)
    
    # Contact fields
    EMAIL = models.EmailField(unique=True, null=False)
    PHONE = models.CharField(max_length=15, null=False)
    
    # Personal info
    DOB = models.DateField(null=True, blank=True)  # Optional date of birth
    GENDER = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    
    # Employee details
    EMP_ID = models.CharField(max_length=6, unique=True, null=False)  # Ensure at least 6 characters
    DEPT_NAME = models.CharField(max_length=50, null=False)
    DESIGNATION = models.CharField(max_length=50, null=False)
    DATE_OF_JOINING = models.DateField(null=False)
    EMP_TYPE = models.CharField(max_length=10, choices=[('Full-Time', 'Full-Time'), ('Part-Time', 'Part-Time')], null=False)
    
    # Address info
    ADDRESS = models.CharField(max_length=200, null=True, blank=True)
    CITY = models.CharField(max_length=50, null=True, blank=True)
    POSTAL_CODE = models.CharField(max_length=10, null=True, blank=True)
    
    # Status
    STATUS = models.BooleanField(default=True)  # Active or not
    
    def _str_(self):
        return f"{self.FIRST_NAME} {self.LAST_NAME} ({self.EMP_ID})"  
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
class University(models.Model):
    university_id = models.AutoField(primary_key=True)  # Unique ID for each university
    name = models.CharField(max_length=255, unique=True)  # Name of the university
    code = models.CharField(max_length=20, unique=True)  # Unique code for the university
    address = models.TextField()  # Address
    website_url = models.URLField()  # Website URL
    accreditation_details = models.TextField()  # Accreditation details
    total_institutes = models.PositiveIntegerField()  # Total number of institutes
    contact_number = models.CharField(max_length=15)  # Contact number
    email = models.EmailField()  # Email
    establishment_year = models.PositiveIntegerField()  # Establishment year
    chancellor_name = models.CharField(max_length=255)  # Chancellor's name

    def __str__(self):
        return self.name
    
class StudentForm(forms.Form):
    first_name=forms.CharField(label='First_Name',max_length=100)
    last_name=forms.CharField(label='Last_Name',max_length=100)
    email =forms.EmailField(label='Email')
    phone = forms.CharField(label='phone',max_length=15)
    date_of_birth=forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type':'date'}))
    gender =forms.ChoiceField(label='Gender',choices=[('M','Male'),('F','Female')])
    student_id=forms.CharField(label='Student_Id',max_length=100)
    department = forms.CharField(label='Department', max_length=100)
    enrollment_date = forms.DateField(label='Enrollment Date', widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(label='Address', widget=forms.Textarea)
    city = forms.CharField(label='City', max_length=100)
    postal_code = forms.CharField(label='Postal Code', max_length=10)
    status = forms.ChoiceField(label='Status', choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=50)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'
