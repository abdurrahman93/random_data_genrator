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
    name = StringGenerator("country")
    date_time=DateGenerator()
    eligible=BooleanGenerator()
    details = Nesting(relation_with=Details)



def create_json_obj(obj, many=False, many_count=0):
    if many:
        temp_list = list()
        for idx in range(many_count):
            temp_list.append(create_json_obj(obj))
        return temp_list
    else:
        temp_dict = dict()
        attr_to_use = {key: value for key, value in vars(obj).items() if not key.startswith('_')}
        for attr_name, attr_obj in attr_to_use.items():
            if isinstance(attr_obj, Nesting):
                temp_dict[attr_name] = create_json_obj(attr_obj.relation_with, many=attr_obj.many,
                                                       many_count=attr_obj.many_count)
            else:
                temp_dict[attr_name] = attr_obj.get_value()
        return temp_dict


result = create_json_obj(Person)
print(result)

def process():

    list_of_objs = list()
    for idx in range(10):
        temp_dict = dict()
        attr_to_use = {key: value for key, value in vars(Person).items() if not key.startswith('_')}
        for attr_name, attr_obj in attr_to_use.items():

            temp_dict[attr_name] = attr_obj.get_value()
        list_of_objs.append(temp_dict)
    print(list_of_objs)
# process()