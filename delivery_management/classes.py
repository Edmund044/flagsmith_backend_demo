from .interfaces import DeliveryManagementPlatform

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
