from .interfaces import DeliveryManagementPlatform,FeatureFlaggingPlatform
from flagsmith import Flagsmith
import json
class Bringg(DeliveryManagementPlatform):
    def get_optimal_route(self):
        return "Using Route Optimiztion from Bringg"

    def automatically_dispatch(self):
        return "Using Auto Dispatch from Bringg"

    def manage_driver(self):
        return "Using Driver management from Bringg"

    def manage_return(self):
        return "Using Returns management from Bringg"

    def manage_multicarrier(self):
        return "Using Multicarrier management from Bringg"

    def track_delivery_in_real_time(self):
        return "Using Real time delivery from Bringg"



class Tookan(DeliveryManagementPlatform):
    def get_optimal_route(self):
        return "Using Route Optimiztion from Tookan"

    def automatically_dispatch(self):
        return "Using Auto Dispatch from Tookan"

    def manage_driver(self):
        return "Using Driver management from Tookan"

    def manage_return(self):
        return "Using Returns management from Tookan"

    def manage_multicarrier(self):
        return "Using Multicarrier management from Tookan"

    def track_delivery_in_real_time(self):
        return "Using Real time delivery from Tookan"
    


class Flagsmith(FeatureFlaggingPlatform):
    def __init__(self) -> None:
        self.flagsmith = Flagsmith(environment_key="cs2AND5kwMtaP3oGP3uLGP")
        self.flags = self.flagsmith.get_environment_flags()

    def get_feature_flag_status(self,flag_value):
        flagsmith = Flagsmith(environment_key="cs2AND5kwMtaP3oGP3uLGP")
        flags = flagsmith.get_environment_flags()
        return flags.is_feature_enabled(flag_value)

    def get_feature_flag_value(self,flag_value):
        return json.loads(self.flags.get_feature_value(flag_value))

