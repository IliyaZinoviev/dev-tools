from datetime import date, datetime
from decimal import Decimal
from typing import Union

import inflect

from helpers import call_multiple_assert
from utils import is_camel, is_snake, convert2snake, convert2camel


class PydanticModelsGenerator:
    inflect_engine: inflect.engine = inflect.engine()

    def __init__(self, input_data: dict = None, root_model_name: str = None, output_path_dir: str = None):
        call_multiple_assert(('input_data', input_data), ('root_model_name', root_model_name),
                             ('output_path_dir', output_path_dir))
        self.models: dict[str, list[str]] = {}
        self.input_data: dict = input_data
        self.root_model_name: str = root_model_name
        self.output_path_dir: str = output_path_dir

    def _get_field_type(self, val: Union[dict, str, int, float, bool], alias: str, is_seq_element: bool = False):
        if isinstance(val, dict):
            res = self._generate_pydantic_model_hierarchy(val, alias, is_seq_element)
        elif isinstance(val, bool):
            res = 'bool'
        elif isinstance(val, str):
            res = 'str'
        elif isinstance(val, int):
            res = 'int'
        elif isinstance(val, float):
            res = 'float'
        elif isinstance(val, Decimal):
            res = 'Decimal'
        elif isinstance(val, datetime):
            res = 'datetime'
        elif isinstance(val, date):
            res = 'datetime'
        else:
            res = 'Any'
        return res

    def _generate_pydantic_model_hierarchy(self, input_data: dict, class_name: str, is_seq_element: bool = False):
        #  todo investigate how to add Optional
        parent_model: str
        class_name_issue_comment: str = ''
        if 'id' in input_data and isinstance(input_data['id'], int):
            input_data.pop('id')
            parent_model = 'IdSchema'
        else:
            parent_model = 'AliasModel'
        if is_camel(class_name):
            first, *others = class_name
            class_name = ''.join([first.title()] + others)
        elif is_snake(class_name):
            first, *others = convert2camel(class_name)
            class_name = ''.join([first.title()] + others)
        else:
            class_name = class_name
        if is_seq_element:
            if singular_noun := self.inflect_engine.singular_noun(class_name):
                class_name = singular_noun
            class_name_issue_comment = '  # todo check/select correct singular noun.'
        header = f'class {class_name}({parent_model}):{class_name_issue_comment}\n'
        if class_name not in self.models:
            self.models[class_name] = [header]
            for alias, val in input_data.items():
                if isinstance(val, list):
                    list_val = val[0]
                    list_field_type = self._get_field_type(list_val, alias, True)
                    field_type = f'list[{list_field_type}]'
                else:
                    field_type = self._get_field_type(val, alias)
                if not is_snake(alias):
                    field_name = convert2snake(alias)
                    line = f'\t{field_name}: {field_type} = Field(alias=\'{alias}\')\n'
                else:
                    field_name = alias
                    line = f'\t{field_name}: {field_type}\n'
                self.models[class_name].append(line)
            self.models[class_name].append('\n\n')
        return class_name

    def exec(self):
        self._generate_pydantic_model_hierarchy(self.input_data, self.root_model_name)
        file_name = convert2snake(self.root_model_name)
        with open(f'{self.output_path_dir}/{file_name}.py', 'a') as file:
            for model in list(self.models.values())[::-1]:
                file.writelines(model)


if __name__ == '__main__':
    input_data = {}
    root_model_name = 'ClassName'
    output_path_dir = ''
    PydanticModelsGenerator(input_data, root_model_name, output_path_dir).exec()
