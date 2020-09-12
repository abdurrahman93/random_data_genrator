import random
from abstract_base import RuleBase


class IntegerRule(RuleBase):

    def __init__(self, start=0, end=0):
        if start and end:
            self._object_type = int
            self.start = start
            self.end = end 
        else:
            raise ValueError(f"Star  and End are required")

    @property
    def object_type(self):
        return self._object_type

    
    def get_value(self):
        return random.randint(self.start, self.end)