from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tops/', views.tops, name='tops'),
    path('bases/',views.bases,name='bases'),
    path('gels/',views.gels,name='gels'),
    path('gelpolish/',views.gelpolish,name='gelpolish'),
    path('description/<int:pk>/',views.description,name='description')
]

