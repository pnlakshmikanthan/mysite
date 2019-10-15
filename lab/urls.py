from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vue/',TemplateView.as_view(template_name='vue.html')),
    path('signup/',views.signup, name='signup'),
   
]