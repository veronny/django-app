from django.urls import path
from . import views

app_name = 'GestanteApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('gestante/', views.TestView.as_view(), name='gestante'),
    path('gestante-filter/', views.filter_gestante, name='filter_gestante'),
    #violencia
    path('violencia/', views.ViolenciaView.as_view(), name='violencia'),
    path('violencia-filter/', views.filter_violencia, name='filter_violencia'),
    #paquete niño
    path('nino/', views.NinoView.as_view(), name='nino'),
    path('nino-filter/', views.filter_nino, name='filter_nino'),
    #CRED
    path('cred/', views.CredView.as_view(), name='cred'),
    path('cred-filter/', views.filter_cred, name='filter_cred'),
]