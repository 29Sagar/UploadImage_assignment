from django.urls import path
from . import views

urlpatterns = [  
    path('upload_image/', views.ImageViewSet.as_view(), name='upload'),
]  