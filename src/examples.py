"""
Some example how to use the library
"""

import pprint
import random
from pathlib import Path
from rule_classes import ObjectValidator, IntegerGenerator, StringGenerator, BooleanGenerator, DateGenerator, \
    Nesting, UUIDGenerator
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
    details = Nesting(relation_with=Details)


data_generator_ins = RandomDataGenerator()
data_generator_ins.generate_csv(Person, 4, Path(__file__).parent)
pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(next(data_generator_ins._generate_data(Person)))
