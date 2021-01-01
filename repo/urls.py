from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='dashboard'),
    path('upload/', views.upload,name= 'upload'),
    path('delete_img/<str:pk>/', views.deleteImage, name="delete_image")
]
