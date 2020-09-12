import random
from abstract_base import DataGeneratorBase


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


class Nesting:

    def __init__(self, relation_with, no_of_relations):
        self.relation_with = relation_with
        self.no_of_relations = no_of_relations



