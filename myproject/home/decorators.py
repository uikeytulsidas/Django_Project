from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:  # Assuming admin has `is_staff` set to True
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You are not authorized to view this page.")
    return wrapper_func

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
         if request.user.is_authenticated:
             return redirect('welcome')
         else:
        
             return view_func (request, *args,**kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request ,*args,**kwargs):
             
           print('working')  
           group=None
           if request.user.group.exists():
               group =request.user.group.all()[0].name
           if group in allowed_roles:
                return view_func (request, *args,**kwargs)
           else:
               return HttpResponse('You are not authorized')
               return  wrapper_func
        return decorator
    
        