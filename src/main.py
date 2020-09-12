from rule_classes import IntegerGenerator, Nesting


class Details:

    money = IntegerGenerator(start=1000, end=20000)


class Person:

    age = IntegerGenerator(start=1, end=10)
    phone_no = IntegerGenerator(start=9000000010, end=9999999999)
    # details = Nesting(relation_with=Details, no_of_relations=4)


def create_json_obj(obj):
    temp_dict = dict()
    attr_to_use = {key: value for key, value in vars(obj).items() if not key.startswith('_')}
    for attr_name, attr_obj in attr_to_use.items():


        temp_dict[attr_name] = attr_obj.get_value()


def process():

    list_of_objs = list()
    for idx in range(10):
        temp_dict = dict()
        attr_to_use = {key: value for key, value in vars(Person).items() if not key.startswith('_')}
        for attr_name, attr_obj in attr_to_use.items():

            temp_dict[attr_name] = attr_obj.get_value()
        list_of_objs.append(temp_dict)
    print(list_of_objs)
process()