import re
from itertools import chain
from typing import Optional, Match, AnyStr

from utils import is_camel, is_snake, convert2snake


class PydanticModelsGenarator:
    def __init__(self, input_data: dict, root_model_name: str):
        self.models: dict[str, list[str]] = {}
        self.input_data: dict = input_data
        self.root_model_name: str = root_model_name

    def _generate_pydantic_model_hierarchy(self, input_data: dict, name: str):
        #  todo investigate how to add Optional
        parent_model: str
        if 'id' in input_data and isinstance(input_data['id'], int):
            input_data.pop('id')
            parent_model = 'IdSchema'
        else:
            parent_model = 'AliasModel'
        if is_camel(name):
            first, *others = name
            class_name = ''.join([first.title()] + others)
        else:
            class_name = name
        header = f'class {class_name}({parent_model}):\n'
        if class_name not in self.models:
            self.models[class_name] = [header]
            for alias, val in input_data.items():
                if isinstance(val, dict):
                    field_type = self._generate_pydantic_model_hierarchy(val, alias)
                elif isinstance(val, list):
                    list_val = val[0]
                    if isinstance(list_val, dict):
                        list_field_type = self._generate_pydantic_model_hierarchy(val[0], alias)
                    elif isinstance(val, str):
                        list_field_type = 'str'
                    elif isinstance(val, int):
                        list_field_type = 'int'
                    elif isinstance(val, float):
                        list_field_type = 'Decimal'
                    else:
                        list_field_type = 'Any'
                    field_type = f'list[{list_field_type}]'
                elif isinstance(val, str):
                    field_type = 'str'
                elif isinstance(val, int):
                    field_type = 'int'
                elif isinstance(val, float):
                    field_type = 'Decimal'
                else:
                    field_type = 'Any'
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
        self._generate_pydantic_model_hierarchy(input_data, root_model_name)
        file_name = convert2snake(root_model_name)
        with open(f'{file_name}.py', 'a') as file:
            for model in list(self.models.values())[::-1]:
                file.writelines(model)


if __name__ == '__main__':
    input_data = {}
    root_model_name = 'ClassName'
    PydanticModelsGenarator(input_data, root_model_name)
