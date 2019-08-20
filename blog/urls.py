from django.urls import path
from . import views


urlpatterns = [
     path ('',views.mostrar,name = 'list_posts')
 ]