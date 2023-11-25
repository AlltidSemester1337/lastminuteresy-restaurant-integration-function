from abc import abstractmethod, ABC

from model.booking_failed_exception import BookingFailedException


class Integration(ABC):
    @abstractmethod
    def attempt_booking(self, restaurant, time, num_persons, extra_parameters):
        pass

    @staticmethod
    def verify_mandatory_parameters(mandatory_parameters: dict, extra_parameters: dict):
        for e in mandatory_parameters:
            type(extra_parameters.get(e))
            expected_type = mandatory_parameters[e]
            if extra_parameters.get(e) is None or not expected_type == type(extra_parameters[e]):
                raise BookingFailedException(
                    "Could not find or type mismatch for mandatory parameter: " + str(
                        e) + ", expected " + str(expected_type))
