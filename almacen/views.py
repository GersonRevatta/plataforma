from django.shortcuts import render, redirect #puedes importar render_to_response
from .form import cursos
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from usuario.models import usuario
from django.core.urlresolvers import reverse
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


