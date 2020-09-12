import random
from rule_classes import IntegerRule


class DummyObj:

    age = IntegerRule(start=1, end=10)
    phone_no = IntegerRule(start=9000000010, end=9999999999)


def process():

    list_of_objs = list()
    for idx in range(10):
        temp_dict = dict()
        attr_to_use =  {key: value for key, value in vars(DummyObj).items() if not key.startswith('_')} 
        for attr_name, attr_obj in attr_to_use.items():
            temp_dict[attr_name] = attr_obj.get_value()
        list_of_objs.append(temp_dict)
    print(list_of_objs)
process()