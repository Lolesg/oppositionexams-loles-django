from django.contrib.auth.backends import UserModel
from django.shortcuts import render
from .models import *

from django.views import generic
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from preguntas.models import Pregunta,Respuesta
from resultados.models import Resultado

# Create your views here.

def index(request):
    categoria = Categoria.objects.all()
    context = {'categorias':categoria}
    return render(request,'index.html',context)

def lista_examenes(request):
    examen_policia = Examen.objects.filter(categoria=1)
    examen_guardia = Examen.objects.filter(categoria=2)
    context = {'examen_policia':examen_policia,'examen_guardia':examen_guardia}
    return render(request,'lista.html',context)
def examen_view(request,pk):
    examen = Examen.objects.get(pk=pk)
    return render(request,'examen.html',{'obj':examen})

def ver_datos_view(request,pk):
    examen = Examen.objects.get(pk=pk)
    preguntas = []
    for p in examen.get_preguntas():
        respuestas = []
        for r in p.get_respuestas():
            respuestas.append(r.respuesta)
        preguntas.append({str(p):respuestas})
    return JsonResponse({
        'data':preguntas,
        'time':examen.tiempo,
    })

from datetime import date 
from datetime import datetime

def guardar_examen_view(request,pk):
    if request.is_ajax():
        preguntas = []
        data = request.POST 
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for q in data_.keys():
            pregunta = Pregunta.objects.get(texto=q)
            preguntas.append(pregunta)

            
            
        usuario = request.user 
        examen = Examen.objects.get(pk=pk)

        score = 0
        total = 0
        numero_preguntas = examen.numero_de_preguntas
        numero_errores = 0
        numero_aciertos = 0
        pregu = 10/numero_preguntas
        multiplier = 100/examen.numero_de_preguntas
        resultados = []
        respuesta_correcta = None 
        no_sabe=0
        for p in preguntas:
            r_selected = request.POST.get(str(p))
            if r_selected !="":
                respuesta_pregunta = Respuesta.objects.filter(pregunta=p)
                for a in respuesta_pregunta:
                    if r_selected == a.respuesta:
                        if a.correcta:
                            score +=1
                            numero_aciertos +=1
                            respuesta_correcta = a.respuesta
                    elif r_selected =='NS/NC':
                        if a.correcta:
                            no_sabe +=1
                            respuesta_correcta = a.respuesta 
                    else:
                        if a.correcta:
                            numero_errores += 1
                            respuesta_correcta = a.respuesta 
                resultados.append({str(p):{'Respuesta_correcta':respuesta_correcta,'respuesta':r_selected}})
            else:
                resultados.append({str(p):'No respondida'})
        score_=score*multiplier
        mal = float(numero_errores/2)
        total=float((numero_aciertos-mal)*pregu)
        fecha_examen=datetime.now()
        if total<0:
            total=0
        Resultado.objects.create(examen=examen,usuario=usuario,nota=total,fecha=fecha_examen)

        if total>=examen.puntuacion_para_pasar:
            return JsonResponse({'pasar':True,'nota':total,'resultados':resultados})
        else:
            return JsonResponse({'pasar':False,'nota':total,'resultados':resultados})

from django.contrib.auth import login 
from django.shortcuts import redirect, render 
from django.urls import reverse 
from examenes.forms import CustomerUserCreationForm

def register(request):
    if request.method == "GET":
        return render(
            request,"oppositionexams/register.html",
            {"form":CustomerUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
        return redirect('oppositionexams:index')




def policia(request):
    examen_policia = Examen.objects.filter(categoria=1)
    context = {'examen_policia':examen_policia}
    return render(request,'oppositionexams/policia.html',context)
def guardia(request):
    examen_guardia = Examen.objects.filter(categoria=2)
    context = {'examen_guardia':examen_guardia}
    return render(request,'oppositionexams/guardia.html',context)
def policia_conociiento(request):
    examen = Examen.objects.filter(categoria=1)
    examen_policia=examen.filter(sub_categoria=1)
    context = {'examen_policia':examen_policia}
    return render(request,'oppositionexams/pconocimiento.html',context)
def policia_ortografia(request):
    examen = Examen.objects.filter(categoria=1)
    examen_policia=examen.filter(sub_categoria=2)
    context = {'examen_policia':examen_policia}
    return render(request,'oppositionexams/portografia.html',context)
def policia_psicotecnico(request):
    examen = Examen.objects.filter(categoria=1)
    examen_policia=examen.filter(sub_categoria=5)
    context = {'examen_policia':examen_policia}
    return render(request,'oppositionexams/ppsicotecnico.html',context)
def guardia_conocimiento(request):
    examen = Examen.objects.filter(categoria=2)
    examen_guardia = examen.filter(sub_categoria=3)
    context = {'examen_guardia':examen_guardia}
    return render(request,'oppositionexams/gconocimiento.html',context)
def guardia_ortografia(request):
    examen = Examen.objects.filter(categoria=2)
    examen_guardia = examen.filter(sub_categoria=4)
    context = {'examen_guardia':examen_guardia}
    return render(request,'oppositionexams/gortografia.html',context)
def guardia_psicotecnico(request):
    examen = Examen.objects.filter(categoria=2)
    examen_guardia = examen.filter(sub_categoria=6)
    context = {'examen_guardia':examen_guardia}
    return render(request,'oppositionexams/gpsicotecnico.html',context)


def perfil(request):
    usuario = request.user
    resultados = Resultado.objects.filter(usuario=usuario)
    resultao=resultados.all()
    context = {'usuario':usuario,'resultados':resultao}
    return render(request,'oppositionexams/perfil.html',context)

'''

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
'''

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

UserModel = get_user_model()
from .forms import SignupForm
from .tokens import account_activation_token

from django.core.mail import send_mail
from django.conf import settings

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            subject = "Confirmación Registro"
            current_site = get_current_site(request)
            mensaje = render_to_string('acc_active_email.html',{
                'user':user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            message = mensaje
            email_from = settings.EMAIL_HOST_USER
            recipient_list = request.POST["email"]
            send_mail(subject,message,email_from,[recipient_list])
            return HttpResponse('Por favor confirma tu dirección de correo para completar el registro')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        direccion="{% url 'oppositionexams:index' %}"
        response = HttpResponse()
        response.write("Gracias por confirmar tu correo. Haz click en el siguiente enlace para terminar <a href="+direccion+">Página de Inicio</a>")
        return render(request,'index.html',{'response':response})
    else:
        return HttpResponse('Activation link is invalid!')

from .forms import ContactForm
def nosotros(request):
    if request.method == 'GET':
        form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            mensaje = 'El usuario: '+name+' con el siguiente correo electrónico '+from_email+' \nHa mandado un mensaje mediante el formulario de contacto con el asunto: '+subject+' \nEl mensaje es el siguiente:\n'+message
            try:
                send_mail(subject,mensaje,from_email,['oppositionexams@gmail.com'])
            except:
                return HttpResponse('Formulario no válido')
    return render(request,'nosotros.html',{'form':form})
            
    
