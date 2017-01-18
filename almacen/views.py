from django.shortcuts import render, redirect #puedes importar render_to_response
#from .form import cursos ,capitulos , CommentForm ,ReplyForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from usuario.models import usuario
from django.core.urlresolvers import reverse
#from .models import Cursos ,Comment
import hashlib
from django.template.context_processors import csrf
from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso , Tema , Video ,Comment,Categoria
from .form import CursoForm,TemaForm,VideoForm,CommentForm,CategoriaForm

#from .models import Document

def creandoCursos(request):
	if request.POST:
		frm=CursoForm(request.POST,request.FILES)
		fr=CategoriaForm(request.POST)
		if frm.is_valid() and fr.is_valid():
			a = frm.save()
			b=fr.save()
			try:
				a.usuario = usuario.objects.get(username=request.session['userr'])
				a.categoria=Categoria.objects.get(id=b.id)

			except KeyError:
				pass
			a.codigo = hashlib.md5(str(a.id).encode()).hexdigest()[:5]	
			a.save()


		
		
	fr = CategoriaForm()
	frm = CursoForm()
	try:
		lis = usuario.objects.get(username=request.session['userr'])
		ls = Curso.objects.all()	
		
	except :
		pass
	context = {'frm':frm,'fr':fr,'lis':lis,'ls':ls}
			

	return render(request,'addcurso.html',context)
'''
try:		
		lis = usuario.objects.get(username=request.session['userr'])
		ls = Cursos.objects.all()	
		if lis.gender == 't':
			return render(request,'cursos.html', {'lis':lis,'ls':ls})
	except :
			pass
	return render(request,'cursos.html', {'ls':ls})	

'''

'''	
	if request.POST:
		frm=cursos(request.POST,request.FILES)
		if frm.is_valid():
			a = frm.save()
			try:
				a.usuario = usuario.objects.get(username=request.session['userr'])

			except KeyError:
				pass
			a.codigo = hashlib.md5(str(a.id).encode()).hexdigest()[:5]	
			a.save()

		
		return HttpResponseRedirect(reverse('miscursos'))
		#return HttpResponse('curso agregado')
		
	else:
		frm = cursos()
		args = {}
		args.update(csrf(request))
		args['frm'] = frm
		return render(request,'addcurso.html',args)

'''
#verificado
'''

def miscursos(request):
	try:
		listar = usuario.objects.get(username=request.session['userr'])
		alistar = Curso.objects.filter(usuario=listar)
	except KeyError:
		pass
	return	render(request,'miscursos.html',{'alistar':alistar})	

'''
#TemaForm,VideoForm
def addcapitulo(request):
	try:
		listar = usuario.objects.get(username=request.session['userr'])
		alistar = Curso.objects.filter(usuario=listar)
	except KeyError:
		pass

	if request.POST:
		frm=CursoForm(request.POST,request.FILES)
		fr=CategoriaForm(request.POST)
		if frm.is_valid() and fr.is_valid():
			a = frm.save()
			b=fr.save()
			try:
				a.usuario = usuario.objects.get(username=request.session['userr'])
				a.categoria=Categoria.objects.get(id=b.id)

			except KeyError:
				pass
			a.codigo = hashlib.md5(str(a.id).encode()).hexdigest()[:5]	
			a.save()

	fr = CategoriaForm()
	frm = CursoForm()
	context={'frm':frm,'fr':fr,'listar':listar,'alistar':alistar}
	return render (request,'addcapitulo.html',context)		
'''				
	if request.POST and alistar.id:
		frm=VideoForm(request.POST,request.FILES)
		fr = TemaForm(request.POST)
		if frm.is_valid() and fr.is_valid():
			b=frm.save()
			a=fr.save()
			a.id=get_object_or_404(Curso, pk=alistar.id)
			try:
				#b.curso = get_object_or_404(Curso, codigo=codigo)
				
				#b.codigo = codigo
				
				pass
			except KeyError:
				pass	

'''				

	

				
	#frm=VideoForm()
	#fr=TemaForm()
	

	
def creandoCapitulos(request,codigo):
	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid() :
			b=form.save()
			
			a= Tema.objects.filter(codigo=codigo)
			for repo in a:
				b.tema = get_object_or_404(Tema,id=repo.id)
			
			b.save()    
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
		
		j= Curso.objects.get(codigo=codigo)
		c = Tema.objects.filter(codigo = j.codigo )
		d= Video.objects.all()
		co=Comment.objects.all()
		
	except KeyError:
		pass	
	form=CommentForm()	
	frm=VideoForm()
	fr=TemaForm()
	context={'frm':frm,'fr':fr,'c':c,'d':d,'form':form,'co':co}
	return render(request,'addtema.html',context)		
'''	

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



	if request.POST:
		frm=capitulos(request.POST,request.FILES)
		if frm.is_valid():
			b=frm.save()
			try:
				b.curso = get_object_or_404(Cursos, codigo=codigo)
				b.codigo = codigo
				
				pass
			except KeyError:
				pass	
			b.save()

			return HttpResponseRedirect(reverse('miscursos'))
			
			
	else:
		frm=capitulos()

		return render (request,'addcapitulo.html',{'frm':frm})		
'''


def add_comment(request, id_video):
	ls = Comment.objects.all()	
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.document= get_object_or_404(Document,pk=id_video)
			comment.save()


			
	form =CommentForm()
	template = 'comentario.html'
	context = {'form':form,'ls':ls}
	return render(request,template,context)
		

def mostrarComentario(request):
	ls = Comment.objects.all()	
	return render(request,'mostrarcomentario.html',{'ls':ls})














