import random
import uuid
from pathlib import Path
import datetime
from base_class import DataGeneratorBase


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
        self.input = input

    @property
    def object_type(self):
        return self._object_type

    def validate(self):
        pass

    def get_value(self):
        if isinstance(self.input, list):
            return random.choice(self.input)
        if isinstance(self.input, str):
            file_path = Path.joinpath(Path().absolute().parent, Path("data_sets"), Path(f"{(self.input).lower()}.txt"))
            with open(file_path, 'r') as a:
                return (random.choice(list(a))).strip()


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


class DateGenerator(DataGeneratorBase):

    def __init__(self, start=None, end=None, format="%Y-%m-%d"):
        self._object_type = datetime.datetime
        self.format = format
        if start and end:
            self.start = datetime.datetime.strptime(start, self.format)
            self.end = datetime.datetime.strptime(end, self.format)
        else:
            self.start = (datetime.datetime(1950, 1, 1).date())
            self.end = (datetime.datetime.now().date())

    @property
    def object_type(self):
        return self._object_type

    def validate(self):
        pass

    def get_value(self):
        time_between_dates = self.end - self.start
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = self.start + datetime.timedelta(days=random_number_of_days)
        return random_date.strftime(self.format)


class UUIDGenerator(DataGeneratorBase):

    def __init__(self):
        self._object_type = type(uuid.uuid4())

    @property
    def object_type(self):
        return self._object_type

    def validate(self):
        pass

    def get_value(self):
        return str(uuid.uuid4())


class Nesting:

    def __init__(self, relation_with, many=False, many_count=0):
        self.relation_with = relation_with
        self.many = many
        self.many_count = many_count
        self.relate_by = 'id'

    def validate(self):
        if not self.relate_by:
            raise ValueError('relate_by cannot be empty or none')
        elif type(self.relate_by) is not str:
            raise ValueError('relate_by should be str type')


class ObjectGenerator:

    @staticmethod
    def _check_if_object_has_nesting(attr_to_use):
        for attr_name, attr_obj in attr_to_use.items():
            if isinstance(attr_obj, Nesting):
                return True
        return False

    @classmethod
    def _validate(cls):
        attr_to_use = {key: value for key, value in vars(cls).items() if not key.startswith('_')}
        if cls._check_if_object_has_nesting(attr_to_use):
            if 'id' not in attr_to_use.keys():
                raise ValueError(f"{cls.__name__} have nesting should have id attribute")

        for attr_name, attr_obj in attr_to_use.items():
            attr_obj.validate()
            if isinstance(attr_obj, Nesting):
                attr_obj.relation_with._validate()