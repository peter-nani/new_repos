
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('list', views.ob_all, name='list'),
    path('update/<str:id>/', views.obj_edit, name='update'),
    path('delete/<str:id>/', views.delet, name='delete'),
]

