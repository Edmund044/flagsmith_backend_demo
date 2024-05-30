from abc import ABC,abstractmethod

class DeliveryManagementPlatform(ABC):
    @abstractmethod
    def route_optimization(self):
        pass

    @abstractmethod
    def auto_dispatch(self):
        pass

    @abstractmethod
    def driver_management(self):
        pass

    @abstractmethod
    def returns_management(self):
        pass

    @abstractmethod
    def multicarrier_management(self):
        pass

    @abstractmethod
    def checkout_experience(self):
        pass

    @abstractmethod
    def real_time_delivery(self):
        pass


class Bringg(RouteOptimzer):
    def route_optimization(self):
        pass

    def auto_dispatch(self):
        pass

    def driver_management(self):
        pass

    def returns_management(self):
        pass

    def multicarrier_management(self):
        pass

    def checkout_experience(self):
        pass

    def real_time_delivery(self):
        pass



class Tookan(RouteOptimzer):
    def route_optimization(self):
        pass

    def auto_dispatch(self):
        pass

    def driver_management(self):
        pass

    def returns_management(self):
        pass

    def multicarrier_management(self):
        pass

    def checkout_experience(self):
        pass

    def real_time_delivery(self):
        pass



class User():
    def __init__(self,delivery_platform:DeliveryManagementPlatform):
        self.delivery_platform = delivery_platform

    def get_optimal_route(self):
        return self.delivery_platform.route_optimization()
    


    