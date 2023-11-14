from abc import abstractmethod, ABC


class Integration(ABC):
    @abstractmethod
    def attempt_booking(self, restaurant, time):
        pass
