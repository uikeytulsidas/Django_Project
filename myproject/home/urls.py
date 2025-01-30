from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    
    path('login/',views.login, name='login'),
    # path('logout/', views.custom_logout_view, name='logout'),
      path('logout/', views.logout_view, name='logout'),  # Logout page
     path('', views.home, name='welcome'),
    path('create/', views.create_item, name='create_item'),
    path('update/<int:pk>/', views.update_item, name='update_item'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="home/password_reset_form.html",
                                                                 email_template_name="home/password_reset_email.html"), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="home/password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="home/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="home/password_reset_complete.html"), name='password_reset_complete'),
    path('employee-form/', views.employee_form, name='employee_form'),
    path('employee-success/', views.employee_success, name='employee_success'),  # Success page
    path('student-form/', views.student_form, name='student_form'),
     path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
     # Admin Dashboard
    path('profile/', views.profile_view, name='profile'),
     
   # path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Student Management
   # path('admin/students/', views.admin_student_list, name='admin_student_list'),
    #path('admin/students/add/', views.admin_add_student, name='admin_add_student'),
    #path('admin/students/update/<int:pk>/', views.admin_update_student, name='admin_update_student'),
   # path('admin/students/delete/<int:pk>/', views.admin_delete_student, name='admin_delete_student'),
    
    
    
]
