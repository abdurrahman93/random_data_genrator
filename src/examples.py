"""
Some example how to use the library
"""

import pprint
import random
from pathlib import Path
from rule_classes import ObjectValidator, IntegerGenerator, StringGenerator, BooleanGenerator, DateGenerator, \
    Nesting, UUIDGenerator, DerivedVal
from random_data_generator import RandomDataGenerator


class AnotherSubDetails(ObjectValidator):
    polo = IntegerGenerator(start=1000, end=20000)


class SubDetails(ObjectValidator):
    id = UUIDGenerator()
    yolo = IntegerGenerator(start=1000, end=20000)
    another_details = Nesting(relation_with=AnotherSubDetails)


class Details(ObjectValidator):
    id = UUIDGenerator()
    money = IntegerGenerator(start=1000, end=20000)
    sub_details = Nesting(relation_with=SubDetails, many=True, many_count=lambda: random.randint(1, 4))


class Person(ObjectValidator):
    id = UUIDGenerator()
    age = IntegerGenerator(start=1, end=10)
    phone_no = IntegerGenerator(start=9000000010, end=9999999999)
    eligible = BooleanGenerator()
    name = StringGenerator("country")
    date_time = DateGenerator()
    details = Nesting(relation_with=Details, many=True, many_count=lambda: random.randint(0, 6))


def custom_fuc(*args, **kwargs):
    return kwargs.get('first_name') + ' YOLOLOLOLO ' + kwargs.get('last_name')


def another_func(*args, **kwargs):
    return kwargs.get('full_name') + ' YOLOLOLOLO '


class AnotherPerson(ObjectValidator):
    first_name = StringGenerator("names")
    last_name = StringGenerator("names")
    full_name = DerivedVal(custom_fuc, order=1)
    full_name_plus = DerivedVal(another_func, order=2)


data_generator_ins = RandomDataGenerator()
# data_generator_ins.generate_csv(4, Person, Path(__file__).parent)
pp = pprint.PrettyPrinter(indent=4)
for data in data_generator_ins.generate_json(2, AnotherPerson):
    pp.pprint(data)

