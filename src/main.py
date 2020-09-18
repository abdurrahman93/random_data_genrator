from pathlib import Path
from openpyxl import Workbook, load_workbook
from rule_classes import ObjectValidator, IntegerGenerator, StringGenerator, BooleanGenerator, DateGenerator, \
    Nesting, UUIDGenerator


class AnotherSubDetails(ObjectValidator):
    polo = IntegerGenerator(start=1000, end=20000)


class SubDetails(ObjectValidator):
    id = UUIDGenerator()
    yolo = IntegerGenerator(start=1000, end=20000)
    another_details = Nesting(relation_with=AnotherSubDetails)


class Details(ObjectValidator):
    id = UUIDGenerator()
    money = IntegerGenerator(start=1000, end=20000)
    sub_details = Nesting(relation_with=SubDetails, many=True, many_count=2)


class Person(ObjectValidator):
    id = UUIDGenerator()
    age = IntegerGenerator(start=1, end=10)
    phone_no = IntegerGenerator(start=9000000010, end=9999999999)
    eligible = BooleanGenerator()
    name = StringGenerator("country")
    date_time = DateGenerator()
    details = Nesting(relation_with=Details)


class RandomDataGenerator:

    def __int__(self):
        pass

    def _generate_data(self, obj, many=False, many_count=0, relate_id=None, relate_name=None):
        if many:
            temp_list = list()
            for idx in range(many_count):
                temp_list.append(next(self._generate_data(obj, relate_id=relate_id, relate_name=relate_name)))
            yield temp_list
        else:
            temp_dict = dict()
            attr_to_use = {key: value for key, value in vars(obj).items() if not key.startswith('_')}
            for attr_name, attr_obj in attr_to_use.items():
                if isinstance(attr_obj, Nesting):
                    temp_dict[attr_name] = next(self._generate_data(attr_obj.relation_with, many=attr_obj.many,
                                                                    many_count=attr_obj.many_count,
                                                                    relate_name=obj.__name__,
                                                                    relate_id=temp_dict.get(attr_obj.relate_by)))
                else:
                    temp_dict[attr_name] = attr_obj.get_value()

            if relate_id and relate_name:
                temp_dict[relate_name.lower() + '_id'] = relate_id

            yield temp_dict

    def _write_csv(self, obj_to_create, obj_name, excel_wb):
        try:
            active_ws = excel_wb[obj_name]
        except KeyError:
            active_ws = excel_wb.create_sheet(title=obj_name)
            active_ws.append([key for key, value in obj_to_create.items() if not isinstance(value, (dict, list))])

        values_to_write = list()
        for attr_name, attr_value in obj_to_create.items():
            if isinstance(attr_value, dict):
                self._write_csv(attr_value, attr_name, excel_wb)
            elif isinstance(attr_value, list):
                for obj in attr_value:
                    self._write_csv(obj, attr_name, excel_wb)
            else:
                values_to_write.append(attr_value)
        active_ws.append(values_to_write)

    def generate_csv(self, obj_to_create, folder_path=Path(r"F:\python_projects\random_data_genrator\src")):
        obj_to_create._validate()
        wb = Workbook()
        excel_name = folder_path.joinpath('data.xlsx')
        for i in range(5):
            data = next(self._generate_data(obj_to_create))
            print(data)
            self._write_csv(data, obj_to_create.__name__, wb)
        wb.save(filename=excel_name.__str__())



            # for data in self._generate_data(obj_to_create):
            # self.write_csv(data, obj_to_create.__name__, folder_path)

import pprint

data_generator_ins = RandomDataGenerator()
data_generator_ins.generate_csv(Person)
#pp = pprint.PrettyPrinter(indent=4)

#pp.pprint(next(data_generator_ins._generate_data(Person)))
