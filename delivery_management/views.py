from django.http import HttpResponse
from .controllers import DeliveryManagementController,FeatureFlagManagementController
from .classes import Tookan,Bringg,Flagsmith
from flagsmith import Flagsmith
import json


# Create your views here.


def choose_strategy(flag_value):
    return Bringg() if flag_value else Tookan() 


def route_optimizer(request):
    is_enabled = FeatureFlagManagementController(Flagsmith()).get_feature_flag_status("use_bringg")
    delivery_platform = choose_strategy(is_enabled)
    return HttpResponse(DeliveryManagementController(delivery_platform).get_optimal_route())
def automatic_dispatcher(request):
    flags = flagsmith.get_environment_flags()
    is_enabled = flags.is_feature_enabled("use_bringg")
    delivery_platform = choose_strategy(is_enabled)
    return HttpResponse(DeliveryManagementController(delivery_platform).automatically_dispatch())
def manage_driver(request):
    flags = flagsmith.get_environment_flags()
    is_enabled = flags.is_feature_enabled("use_bringg")
    delivery_platform = choose_strategy(is_enabled)
    return HttpResponse(DeliveryManagementController(delivery_platform).manage_driver())
def manage_return(request):
    flags = flagsmith.get_environment_flags()
    is_enabled = flags.is_feature_enabled("use_bringg")
    delivery_platform = choose_strategy(is_enabled)
    return HttpResponse(DeliveryManagementController(delivery_platform).manage_driver())
def manage_multicarrier(request):
    flags = flagsmith.get_environment_flags()
    is_enabled = flags.is_feature_enabled("use_bringg")
    delivery_platform = choose_strategy(is_enabled)
    return HttpResponse(DeliveryManagementController(delivery_platform).manage_multicarrier())
def track_delivery_in_real_time(request):
    flags = flagsmith.get_environment_flags()
    is_enabled = flags.is_feature_enabled("use_bringg")
    delivery_platform = choose_strategy(is_enabled)
    return HttpResponse(DeliveryManagementController(delivery_platform).track_delivery_in_real_time())