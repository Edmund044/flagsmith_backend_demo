from django.urls import path
from . import views
    
urlpatterns = [
    path('route-optimizer', views.route_optimizer, name='route-optimizer'),
    path('automatic-dispatch-management', views.automatic_dispatcher, name='automatic-dispatch-management'),
    path('driver-management', views.manage_driver, name='driver-management'),
    path('return-management', views.manage_return, name='return-management'),
    path('multicarrier-management', views.manage_multicarrier, name='multicarrier-management'),
    path('real-time-tracking', views.track_delivery_in_real_time, name='real-time-tracking'),
]
