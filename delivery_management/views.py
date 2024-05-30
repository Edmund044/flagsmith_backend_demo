from django.http import HttpResponse
from .controllers import DeliveryManagementController
from .classes import Tookan,Bringg
from flagsmith import Flagsmith
import json
flagsmith = Flagsmith(environment_key="cs2AND5kwMtaP3oGP3uLGP")

# The method below triggers a network request
flags = flagsmith.get_environment_flags()
# Check for a feature
is_enabled = flags.is_feature_enabled("use_bringg")

# Or, use the value of a feature
# feature_value = json.loads(flags.get_feature_value("banner_size"))

# Create your views here.

print(DeliveryManagementController(Bringg()).get_optimal_route())
print(DeliveryManagementController(Tookan()).automatically_dispatch())  
print(DeliveryManagementController(Bringg()).automatically_dispatch())
print(DeliveryManagementController(Tookan()).manage_driver())  
print(DeliveryManagementController(Bringg()).manage_driver())

def choose_strategy(flag_value):
    return Bringg() if flag_value else Tookan() 


def route_optimizer(request):
    flags = flagsmith.get_environment_flags()
    is_enabled = flags.is_feature_enabled("use_bringg")
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