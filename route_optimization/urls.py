from django.urls import path
from . import views

urlpatterns = [
    path('route-optimizer/', views.route_optimizer, name='route-optimizer'),
]
