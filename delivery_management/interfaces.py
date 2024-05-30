from abc import ABC,abstractmethod

class DeliveryManagementPlatform(ABC):
    @abstractmethod
    def get_optimal_route(self):
        pass

    @abstractmethod
    def automatically_dispatch(self):
        pass

    @abstractmethod
    def manage_driver(self):
        pass

    @abstractmethod
    def manage_return(self):
        pass

    @abstractmethod
    def manage_multicarrier(self):
        pass

    @abstractmethod
    def track_delivery_in_real_time(self):
        pass


class FeatureFlaggingPlatform(ABC):
    @abstractmethod
    def get_feature_flag_status(self):
        pass

    @abstractmethod
    def get_feature_flag_value(self):
        pass


