from django.conf.urls import patterns, url
from project import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
	url(r'^ingresar$', views.ingresar, name='ingresar'),
	url(r'^registrar/$', views.register, name='register'),
	url(r'^salio$', views.salio, name='salio'),
	url(r'^validar$', views.validar, name='validar'),    
	url(r'^proyecto$', views.proyecto, name='proyecto'),    
	url(r'^nuevo_proyecto/$', views.nuevo_proyecto, name='nuevo_proyecto'),    
	url(r'^mis_proyectos/$', views.mis_proyectos, name='mis_proyectos'),    
	url(r'^mis_proyectos/(?P<proyecto_id>\d+)$', views.detalle, name='detalle'),    
	url(r'^mis_proyectos/inicio/(?P<tarea_id>\d+)$', views.inicio, name='inicio'),
	url(r'^mis_proyectos/fin/(?P<tarea_id>\d+)$', views.fin, name='fin'),
	url(r'^nueva_tarea/(?P<proyecto_id>\d+)$', views.nueva_tarea, name='nueva_tarea'),
    url(r'^crear_proyecto$', views.crear_proyecto, name='crear_proyecto'),
    url(r'^nuevo_proyecto/creado/(?P<proyecto_id>\d+)$', views.mostrarProyectoCreado, name='verProyecto'),
)


    