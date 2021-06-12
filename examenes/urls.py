from django.conf.urls import url 
from . import views 
from django.urls import path
from .views import *
from django.urls import include
app_name='oppositionexams'

urlpatterns =[
    url(r'^$',views.index,name="index"),
    url(r'^nosotros/$',views.nosotros,name="nosotros"),
    url(r'^lista/$',views.lista_examenes,name="lista"),
    url(r'^lista/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^lista/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^lista/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
    url(r'^register/$', views.register, name='register'),
    

    url(r'^policia/$',views.policia,name="policia"),
    url(r'^perfil/$',views.perfil,name="perfil"),
    url(r'^policia/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^policia/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^policia/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]
urlpatterns += [
    url(r'^policia/conocimiento/$',views.policia_conociiento,name="pconocimiento"),
    url(r'^policia/conocimiento/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^policia/conocimiento/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^policia/conocimiento/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]

urlpatterns += [
    url(r'^policia/ortografia/$',views.policia_ortografia,name="portografia"),
    url(r'^policia/ortografia/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^policia/ortografia/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^policia/ortografia/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]
urlpatterns += [
    url(r'^policia/psicotecnico/$',views.policia_psicotecnico,name="psicotecnico"),
    url(r'^policia/psicotecnico/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^policia/psicotecnico/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^policia/psicotecnico/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]
urlpatterns += [
    url(r'^guardia/$',views.guardia,name="guardia"),    
    url(r'^guardia/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^guardia/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^guardia/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]

urlpatterns += [
    url(r'^guardia/conocimiento/$',views.guardia_conocimiento,name="gconocimiento"),
    url(r'^guardia/conocimiento/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^guardia/conocimiento/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^guardia/conocimiento/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]
urlpatterns += [
    url(r'^guardia/ortografia/$',views.guardia_ortografia,name="gortografia"),
    url(r'^guardia/ortografia/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^guardia/ortografia/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^guardia/ortografia/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]

urlpatterns += [
    url(r'^guardia/psicotecnico/$',views.guardia_psicotecnico,name="gpsicotecnico"),
    url(r'^guardia/psicotecnico/(?P<pk>\d+)$',views.examen_view,name="examen"),
    url(r'^guardia/psicotecnico/(?P<pk>\d+)/data/$',views.ver_datos_view,name="ver-datos"),
    url(r'^guardia/psicotecnico/(?P<pk>\d+)/save/$',views.guardar_examen_view,name="guardar"),
]

urlpatterns += [
    url(r'^signup/$', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name="activate"),
]
