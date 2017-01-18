from django.shortcuts import render
from .models import usuario
from .form import FormularioRegistro ,FormularioContacto
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import  get_object_or_404
from django.template.context_processors import csrf
# Create your views here.
from django.http import HttpResponse
from almacen.models import Curso ,Document
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required


def registro(request): 
	user=password=''
	if request.POST:
		frm = FormularioRegistro(request.POST)
		if frm.is_valid():
			#verificacion de email
			d=usuario.verificacionEmail(email= request.POST['email'])	
			if d==False:
				#creacion del usuario
				a= usuario.crear( user= request.POST['username'], password =request.POST['password'])
				a.first_name = frm.cleaned_data['first_name']
				a.email = frm.cleaned_data['email']
				a.last_name =frm.cleaned_data['last_name']
				a.dni=frm.cleaned_data['dni']
				a.gender=frm.cleaned_data['gender']
				a.save()
				return HttpResponseRedirect(reverse('loguin'))
				
			else:
				return HttpResponseRedirect(reverse('registro'))			
			
	else:   
		frm = FormularioRegistro()

	args = {}
	args.update(csrf(request))
	args['frm'] = frm
	return render (request,'registro.html',args)

def loguin(request):
	user=password=''
	if request.POST:
		c = FormularioRegistro(request.POST)
		if c.is_valid:
			c  =	usuario.verificar( user= request.POST['username'], password =request.POST['password'])

			if c==True:
				
				z = request.POST['username']		
					#return render(request,test.html,args)
				request.session['userr']=z	
				

				#return HttpResponseRedirect(reverse('create'))
				return HttpResponseRedirect(reverse('index'))

			else:	
				

				return  HttpResponseRedirect(reverse('loguin'))
				
	else:
		c=FormularioRegistro()
	args = {}
	args.update(csrf(request))
	args['c'] = c
	return render(request,'loguin.html',args )



def logout(request):
	try:
		del request.session['userr']
	except KeyError:
		pass
	return  HttpResponseRedirect(reverse('index'))
	



def index(request):
	frm = FormularioRegistro()

	args = {}
	args.update(csrf(request))

	args['frm'] = frm
	
	return render (request,'index.html',args)

#^verificado



def mostrarCurso(request):
	try:		
		lis = usuario.objects.get(username=request.session['userr'])
		ls = Cursos.objects.all()	
		if lis.gender == 't':
			return render(request,'cursos.html', {'lis':lis,'ls':ls})
	except :
			pass
	return render(request,'cursos.html', {'ls':ls})	
	

def miscursos(request):
	try:
		listar = usuario.objects.get(username=request.session['userr'])
		alistar = Curso.objects.filter(usuario=listar)
	except KeyError:
		pass
	return	render(request,'miscursos.html',{'alistar':alistar})	





#verificando
#@login_required(login_url='/sesion')
def mostrar(request,codigo):
	try:

		dato = Cursos.objects.get(codigo=codigo)
		#c = Document.objects.filter(curso = codigo)
		c = Document.objects.filter(codigo=dato.codigo)
		

		
	except KeyError:
		pass   
	#este es el objeto de Cursos
	#c = Document.objects.filter(curso=dato)
	#return HttpResponseRedirect(reverse('must',args=(a.codigo,)))
	#return render_to_response('receta.html',{'receta':dato,'comentarios':comentarios}, context_instance=RequestContext(request))
	return	render(request,'cursoAlgo.html',{'c':c})
'''  
r = reporte.objects.get(codigo=codigo)

	return render (request,'hola.html', {'reporte': r})
'''
#verificado
def contactomail(request):
	if request.method == 'POST':
		formulario = FormularioContacto(request.POST)
		if formulario.is_valid():
			asunto = 'Mensaje de la Aplicacion de django'
			mensaje = formulario.cleaned_data['mensaje']
			mail = EmailMessage(asunto,mensaje,to=['jordyrevatta99@gmail.com'])
			mail.send()
			return HttpResponseRedirect(reverse('index'))
			
	else:	
		formulario = FormularioContacto()
		args = {}
		args.update(csrf(request))
		args['formulario'] = formulario
		return render(request,'contacto.html',args )

