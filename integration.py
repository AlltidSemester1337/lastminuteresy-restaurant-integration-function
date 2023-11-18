from abc import abstractmethod, ABC

from main import BookingFailedException


class Integration(ABC):
    @abstractmethod
    def attempt_booking(self, restaurant, time, extra_parameters):
        pass

    @staticmethod
    def verify_mandatory_parameters(mandatory_parameters, extra_parameters):
        for e in mandatory_parameters:
            expected_type = type(extra_parameters[e])
            if not mandatory_parameters[e].isInstance(expected_type):
                raise BookingFailedException(
                    "Could not find or type mismatch for mandatory parameter: " + e + ", expected " + expected_type)
