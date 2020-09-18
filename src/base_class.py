from abc import abstractmethod, ABC


class DataGeneratorBase(ABC):

    @property
    @abstractmethod
    def object_type(self):
        """Set the object type"""
        pass

    @abstractmethod
    def get_value(self):
        """Calculate a value and return it"""
        pass

    @abstractmethod
    def validate(self):
        """Validate the arguments"""
        pass



