from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import GestanteForm
from .models import Provincia, Distrito, Gestante

from django.http import JsonResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'GestanteApp/index.html'
    
class TestView(TemplateView):
    template_name = 'GestanteApp/gestante.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_provincia_id':
                data = []
                for i in Distrito.objects.filter(cod_prov=request.POST['id']):
                    data.append({'id': i.id, 'name': i.desc_dist})
            else:
                data['error'] = 'Ha occurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Paquete Gestante' 
        context['form'] = GestanteForm()
        context['gestantes'] = Gestante.objects.filter(provincia=2,distrito=1)
        return context
    
def filter_gestante(request):
    if request.method == 'POST':
        provincia = request.POST['provincia']
        distrito = request.POST['distrito'] 
        gestante = Gestante.objects.filter(provincia=provincia,distrito=distrito)
        
        return render(request, 'GestanteApp/gestante-filter.html',{'gestante':gestante})
    else:
        return render(request, 'GestanteApp/gestante-filter.html')
        
#Violencia      
class ViolenciaView(TemplateView):
    template_name = 'GestanteApp/violencia.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_provincia_id':
                data = []
                for i in Distrito.objects.filter(cod_prov=request.POST['id']):
                    data.append({'id': i.id, 'name': i.desc_dist})
            else:
                data['error'] = 'Ha occurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Violencia en Gestante' 
        context['form'] = GestanteForm()
        return context
    
def filter_violencia(request):
    if request.method == 'POST':
        provincia = request.POST['provincia']
        distrito = request.POST['distrito'] 
        gestante = Gestante.objects.filter(provincia=provincia,distrito=distrito)
        
        return render(request, 'GestanteApp/violencia-filter.html',{'gestante':gestante})
    else:
        return render(request, 'GestanteApp/violencia-filter.html')

#nino
class NinoView(TemplateView):
    template_name = 'GestanteApp/nino.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_provincia_id':
                data = []
                for i in Distrito.objects.filter(cod_prov=request.POST['id']):
                    data.append({'id': i.id, 'name': i.desc_dist})
            else:
                data['error'] = 'Ha occurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Paquete integrado del niño' 
        context['form'] = GestanteForm()
        return context
    
def filter_nino(request):
    if request.method == 'POST':
        provincia = request.POST['provincia']
        distrito = request.POST['distrito'] 
        gestante = Gestante.objects.filter(provincia=provincia,distrito=distrito)
        
        return render(request, 'GestanteApp/nino-filter.html',{'gestante':gestante})
    else:
        return render(request, 'GestanteApp/nino-filter.html')

#cred
class CredView(TemplateView):
    template_name = 'GestanteApp/violencia.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_provincia_id':
                data = []
                for i in Distrito.objects.filter(cod_prov=request.POST['id']):
                    data.append({'id': i.id, 'name': i.desc_dist})
            else:
                data['error'] = 'Ha occurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Violencia en Gestante' 
        context['form'] = GestanteForm()
        return context
    
def filter_cred(request):
    if request.method == 'POST':
        provincia = request.POST['provincia']
        distrito = request.POST['distrito'] 
        gestante = Gestante.objects.filter(provincia=provincia,distrito=distrito)
        
        return render(request, 'GestanteApp/violencia-filter.html',{'gestante':gestante})
    else:
        return render(request, 'GestanteApp/violencia-filter.html')

       