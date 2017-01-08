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

from usuario.views import registro, loguin, logout, index,mostrarCurso , miscursos
from almacen.views import creandoCursos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^salir$',logout),
	url(r'^register$',registro,name="registro"),
	url(r'^sesion$',loguin,name="loguin"),
	url(r'^$',index,name="index"),
	url(r'^cursos$',mostrarCurso,name="mostrarCurso"),
	url(r'^addcursos$',creandoCursos,name="creandoCursos"),
	url(r'^my$',miscursos,name="miscursos"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

