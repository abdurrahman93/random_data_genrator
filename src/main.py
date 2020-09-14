from rule_classes import IntegerGenerator, StringGenerator, BooleanGenerator, Nesting
from rule_classes import IntegerGenerator,StringGenerator,BooleanGenerator,DateGenerator, Nesting


class AnotherSubDetails:
    polo = IntegerGenerator(start=1000, end=20000)


class SubDetails:

    yolo = IntegerGenerator(start=1000, end=20000)
    details = Nesting(relation_with=AnotherSubDetails)


class Details:

    money = IntegerGenerator(start=1000, end=20000)
    sub_details = Nesting(relation_with=SubDetails, many=True,  many_count=2)


class Person:

    age = IntegerGenerator(start=1, end=10)
    phone_no = IntegerGenerator(start=9000000010, end=9999999999)
    # name = StringGenerator("random")
    eligible = BooleanGenerator()
    name = StringGenerator("country")
    date_time=DateGenerator()
    eligible=BooleanGenerator()
    details = Nesting(relation_with=Details)


class RandomDataGenerator:

    def __int__(self):
        pass

    def generate_data(self, obj, many=False, many_count=0):
        if many:
            temp_list = list()
            for idx in range(many_count):
                temp_list.append(next(self.generate_data(obj)))
            yield temp_list
        else:
            temp_dict = dict()
            attr_to_use = {key: value for key, value in vars(obj).items() if not key.startswith('_')}
            for attr_name, attr_obj in attr_to_use.items():
                if isinstance(attr_obj, Nesting):
                    temp_dict[attr_name] = next(self.generate_data(attr_obj.relation_with, many=attr_obj.many,
                                                                   many_count=attr_obj.many_count))
                else:
                    temp_dict[attr_name] = attr_obj.get_value()
            yield temp_dict

import pprint


data_generator_ins = RandomDataGenerator()
pp = pprint.PrettyPrinter(indent=4)

pp.pprint(next(data_generator_ins.generate_data(Person, many=True, many_count=4)))
