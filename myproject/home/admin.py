from django.contrib import admin
from .models import University
from .models import Profile


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('university_id', 'name', 'code', 'contact_number', 'email')
    search_fields = ('name', 'code', 'email')
    list_filter = ('establishment_year',)

class AdminArea(admin.AdminSite):
    site_header= 'College Admin'



admin.site.register(Profile)
  
 



# Register your models here.
