import random
from abstract_base import DataGeneratorBase
import names

class IntegerGenerator(DataGeneratorBase):

    def __init__(self, start=0, end=0):
        if start and end:
            self._object_type = int
            self.start = start
            self.end = end
        else:
            raise ValueError(f"Start and End are required")

    @property
    def object_type(self):
        return self._object_type

    def validate(self):
        pass

    def get_value(self):
        return random.randint(self.start, self.end)


class StringGenerator(DataGeneratorBase):

    def __init__(self, input):
        self._object_type = str
        self.input=input

    @property
    def object_type(self):
        return self._object_type

    def validate(self):
        pass

    def get_value(self):
        if isinstance(self.input,list):
            return random.choice(self.input)
        if isinstance(self.input,str):
            return names.get_full_name()



class BooleanGenerator(DataGeneratorBase):

    def __init__(self):
        self._object_type = bool

    @property
    def object_type(self):
        return self._object_type

    def validate(self):
        pass

    def get_value(self):
            return bool(random.getrandbits(1))

class Nesting:

    def __init__(self, relation_with, no_of_relations):
        self.relation_with = relation_with
        self.no_of_relations = no_of_relations
