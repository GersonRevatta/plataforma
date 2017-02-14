from django.contrib import admin

# Register your models here.
from .models import Curso ,Tema ,Categoria
from usuario.models import usuario
#correcto
#class AdminCurso(admin.ModelAdmin):
#	fields = ["name"]
#	list_display = ["name","descripcion"]
#	list_filter = ["categoria"]
#	search_fields = ['name']
#	class Meta:
#		model = Curso

#admin.site.register(Curso,AdminCurso)	



#admin.site.register(Tema , AdminCurso)	
#para queu los campos no se puedan editar
#readonly_fields 




class AdminCurso(admin.ModelAdmin):
	fields = ['name','descripcion']
	list_display = ['name', 'descripcion', 'usuario_username']
	list_filter = ['categoria__nombre']
	search_fields = ['name']
	def usuario_username(self, obj):
		
		#usuario.username.short_username = 'The Author Description'
		return obj.usuario.username
	
	#def categoria_nombre(self, obj):
	 #   return obj.categoria.nombre   
	#categoria_nombre.short_description = 'The Author Description'

	usuario_username.short_description = 'Author'
	

admin.site.register(Curso,AdminCurso)	
#admin.site.register(usuario,AdminCurso)	


