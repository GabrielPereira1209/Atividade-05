from django.contrib import admin
from django.urls import path
from appdoara import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home,name="home"),
  path('formmelhores/', views.create_melhores),
  path('formmortes/', views.create_mortes),
  path('melhores/edit/<melhores_id>', views.update_melhores),
  path('melhores/delete/<melhores_id>', views.delete_melhores),
  path('mortes/edit/<mortes_id>', views.update_mortes),
  path('mortes/delete/<mortes_id>', views.delete_mortes),
]