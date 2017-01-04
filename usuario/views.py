from django.shortcuts import render
from .models import usuario
from .form import FormularioRegistro
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.template.context_processors import csrf
# Create your views here.
from django.http import HttpResponse


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

	return HttpResponse('Saliendo de session ')




def index(request):
	frm = FormularioRegistro()

	args = {}
	args.update(csrf(request))

	args['frm'] = frm
	
	return render (request,'index.html',args)

	
def mostrarCurso(request):
	try:
		lis = usuario.objects.get(username=request.session['userr'])
		
		return render(request,'cursos.html', {'lis':lis})
	except :
			pass
		
	return HttpResponseRedirect(reverse('loguin'))
	
	
''' 
mejorar esto y hacer filtro con los cursos de cada 
		

¿'''
