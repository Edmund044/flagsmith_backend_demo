from .interfaces import DeliveryManagementPlatform,FeatureFlaggingPlatform

class DeliveryManagementController():
    def __init__(self,delivery_platform:DeliveryManagementPlatform):
        self.delivery_platform = delivery_platform

    def get_optimal_route(self):
        return self.delivery_platform.get_optimal_route()
    
    def automatically_dispatch(self):
        return self.delivery_platform.automatically_dispatch()

    def manage_driver(self):
        return self.delivery_platform.manage_driver()

    def manage_return(self):
        return self.delivery_platform.manage_return()

    def manage_multicarrier(self):
        return self.delivery_platform.manage_multicarrier()

    def track_delivery_in_real_time(self):
        return self.delivery_platform.track_delivery_in_real_time()
    

class FeatureFlagManagementController():
    def __init__(self,feature_flag_platform:FeatureFlaggingPlatform):
        self.feature_flag_platform = feature_flag_platform

    def get_feature_flag_status(self,flag_value):
        return self.feature_flag_platform.get_feature_flag_status(flag_value)
    
    def get_feature_flag_value(self,flag_value):
        return self.feature_flag_platform.get_feature_flag_value(flag_value)

    

