from abc import ABCMeta, abstractmethod, ABC, abstractproperty

class RuleBase(ABC):

    @property
    @abstractmethod
    def object_type(self):
        pass
