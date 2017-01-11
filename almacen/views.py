from django.shortcuts import render, redirect #puedes importar render_to_response
from .form import cursos ,capitulos
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from usuario.models import usuario
from django.core.urlresolvers import reverse
from .models import Cursos
import hashlib
from django.template.context_processors import csrf
from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required(login_url='/sesion')
def creandoCursos(request):
	if request.POST:
		frm=cursos(request.POST,request.FILES)
		if frm.is_valid():
			a = frm.save()
			try:
				a.usuario = usuario.objects.get(username=request.session['userr'])

			except KeyError:
				pass
			a.save()

		
		return HttpResponseRedirect(reverse('miscursos'))
		#return HttpResponse('curso agregado')
		
	else:
		frm = cursos()
		return render(request,'addcurso.html', {'frm': frm})

@login_required(login_url='/sesion')
def creandoCapitulos(request,id_curso):
	if request.POST:
		frm=capitulos(request.POST,request.FILES)
		if frm.is_valid():
			b=frm.save()
			try:
				b.curso = get_object_or_404(Cursos, pk=id_curso)
				
				pass
			except KeyError:
				pass	
			b.save()

			return HttpResponseRedirect(reverse('miscursos'))
			
			
	else:
		frm=capitulos()

		return render (request,'addcapitulo.html',{'frm':frm})		




'''


def crear(request):
	if request.POST:
		form = ArticuloForm(request.POST)
		if form.is_valid():
					   

			a = form.save()
			a.codigo = hashlib.md5(str(a.id).encode()).hexdigest()[:5]
			#falta añadir la ruta del modelo para pder utilizarlo con normalidad
			#if request.session['userr']:
			
			 #   a.usuario = request.session['userr']
			#else:
			 #   pass
			 # pedir perdon es mas facil q pedir permiso
			try:
				a.usuario = usuario.objects.get(username=request.session['userr'])
			except KeyError:
				pass


			a.save()

			return HttpResponseRedirect(reverse('must',args=(a.codigo,)))
	else:
		form = ArticuloForm()

	args = {}
	args.update(csrf(request))

	args['form'] = form

	return render(request,'template.html', args)


'''
'''

try:
		listar = usuario.objects.get(username=request.session['userr'])
		alistar = Cursos.objects.filter(usuario=listar)
	except:
		pass
	return	render(request,'miscursos.html',{'alistar':alistar})


class Cursos(models.Model):
	name = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	usuario = models.ForeignKey(usuario,null=True, blank=True)
	imagen = models.ImageField(upload_to='imagenes/')
	

class Document(models.Model):
	titulo = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	filename = models.CharField(max_length=100)
	curso = models.ForeignKey(Cursos,null=True, blank=True)
	docfile = models.FileField(upload_to='document/')
'''
