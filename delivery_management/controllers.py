from .interfaces import DeliveryManagementPlatform

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
    

