# home/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from .models import Employee
from .models import StudentProfile, EmployeeProfile
from .models import Profile


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, required=True)
 


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['FIRST_NAME', 'MIDDLE_NAME', 'LAST_NAME', 'EMAIL', 'PHONE', 'DOB', 'GENDER', 'EMP_ID', 
                  'DEPT_NAME', 'DESIGNATION', 'DATE_OF_JOINING', 'EMP_TYPE', 'ADDRESS', 'CITY', 'POSTAL_CODE', 
                  'STATUS']
# forms.py
from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone', max_length=15)
    date_of_birth = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(label='Gender', choices=[('M', 'Male'), ('F', 'Female')])
    student_id = forms.CharField(label='Student ID', max_length=10)
    department = forms.CharField(label='Department', max_length=100)
    enrollment_date = forms.DateField(label='Enrollment Date', widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(label='Address', widget=forms.Textarea)
    city = forms.CharField(label='City', max_length=100)
    postal_code = forms.CharField(label='Postal Code', max_length=10)
    status = forms.ChoiceField(label='Status', choices=[('Active', 'Active'), ('Inactive', 'Inactive')])


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['user', 'roll_number', 'course']


class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['user', 'department', 'position']

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture']
       
