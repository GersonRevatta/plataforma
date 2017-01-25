from django.shortcuts import render
from .models import usuario,UserProfile
from .form import FormularioRegistro ,FormularioContacto
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import  get_object_or_404
from django.template.context_processors import csrf
# Create your views here.
from django.http import HttpResponse
from almacen.models import Curso ,Document ,Tema
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
import hashlib
import datetime
from django.core.mail import send_mail

import datetime

from django.utils import timezone

import random 
from almacen.form import CursoForm,TemaForm,VideoForm,CommentForm,CategoriaForm
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
				salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:5]            
				activation_key = hashlib.sha1((salt+a.email).encode()).hexdigest() 
				key_expires = datetime.datetime.today() + datetime.timedelta(2)

				#Obtener el nombre de usuario
				user=usuario.objects.get(username=a.username)

				# Crear el perfil del usuario                                                                                                                                 
				new_profile = UserProfile(user=user, activation_key=activation_key, key_expires=key_expires)
				new_profile.save()

			# Enviar un email de confirmación
				email_subject = 'Account confirmation'
				email_body = "Hola %s, Gracias por registrarte. Para activar tu cuenta da clíck en este link en menos de 48 horas: http://127.0.0.1:8000/accounts/confirm/%s" % (a.username, activation_key)

				send_mail(email_subject, email_body, 'jordyrevatta99@gmail.com',[a.email], fail_silently=False)

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
	if 	request.POST:
		frm=VideoForm(request.POST,request.FILES)
		fr = TemaForm(request.POST)
		if frm.is_valid() and fr.is_valid():
			b=frm.save()
			a=fr.save()
			a.curso = get_object_or_404(Curso,codigo=codigo)
			a.codigo=codigo
			b.tema=get_object_or_404(Tema,id=a.id)
			a.save()
			b.save()
	
	try:
		dato = Curso.objects.get(codigo=codigo)
		#c = Document.objects.filter(curso = codigo)
		c = Tema.objects.filter(codigo=dato.codigo)
		lis = usuario.objects.get(username=request.session['userr'])
		
	except KeyError:
		pass
		
	frm = VideoForm()
	fr = TemaForm()
		
	context = {'c':c,'frm':frm,'fr':fr,'lis':lis}
	#este es el objeto de Cursos
	#c = Document.objects.filter(curso=dato)
	#return HttpResponseRedirect(reverse('must',args=(a.codigo,)))
	#return render_to_response('receta.html',{'receta':dato,'comentarios':comentarios}, context_instance=RequestContext(request))
	return	render(request,'cursoAlgo.html',context)
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

def register_confirm(request, activation_key):
	# Verifica que el usuario ya está logeado
	if request.user.is_authenticated():
		HttpResponseRedirect('index')

	# Verifica que el token de activación sea válido y sino retorna un 404
	user_profile = get_object_or_404(UserProfile, activation_key=activation_key)

	# verifica si el token de activación ha expirado y si es así renderiza el html de registro expirado
	if user_profile.key_expires < timezone.now():
		return HttpResponse('ya expiro el tiempo')
	# Si el token no ha expirado, se activa el usuario y se muestra el html de confirmación
	user = user_profile.user
	user.is_active = True
	user.save()
	return HttpResponse('verificacion de cuenta corecta')