"""p_educativa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from usuario.views import registro, loguin, logout, index,mostrarCurso , miscursos , mostrar ,contactomail
from almacen.views import creandoCursos , creandoCapitulos ,add_comment ,mostrarComentario ,addcapitulo
from django.conf import settings
from django.conf.urls.static import static

#from django.contrib.auth.decorators import loguin_required
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^salir$',logout),
	url(r'^register$',registro,name="registro"),
	url(r'^sesion$',loguin,name="loguin"),
	url(r'^$',index,name="index"),
	url(r'^cursos$',mostrarCurso,name="mostrarCurso"),
	url(r'^addcursos$',creandoCursos,name="creandoCursos"),
	url(r'^my$',miscursos,name="miscursos"),
	url(r'^([0-9a-f]{5})$',creandoCapitulos,name="creandoCapitulos"),
	url(r'^mostrarcapitulos/([0-9a-f]{5})$',mostrar,name="mostrar"),
	url(r'^contacto$',contactomail,name="contactomail"),
	url(r'^mostrarcapitulos/comment/(?P<id_video>[0-9])',add_comment,name="add_comment"),
	url(r'^com$',mostrarComentario,name="mostrarComentario"),
	url(r'^addcapitulo$',addcapitulo,name="addcapitulo"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

