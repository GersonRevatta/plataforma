from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import usuario

class AdminUser(admin.ModelAdmin):
	fields = ['username','email','first_name','last_name','dni','acceso']
	list_display = ["username","email",'first_name','last_name','dni']
	list_filter = ["gender"]
	search_fields = ['username']
	class Meta:
		model = usuario
admin.site.register(usuario,AdminUser)	