import json
from typing import TextIO

from pytestgen.dev_middleware import MockSchema


class MockGenerator:
    @staticmethod
    def generate_mock(obj: dict, file: TextIO):
        mock_data = MockSchema(**obj)
        if mock_data.return_value:
            mock_arg_var_name: str = f'{mock_data.mocked_obj_var_name}_return_val'
            mock_arg = f'{mock_arg_var_name} = {mock_data.return_value}\n'
        else:
            mock_arg_var_name: str = f'{mock_data.mocked_obj_var_name}_side_effect'
            mock_arg = f'{mock_arg_var_name} = {mock_data.side_effect}'
        mock_var_name: str = f'{mock_data.mocked_obj_var_name}_mock'
        mock_obj = f'{mock_var_name} = ' \
                   f'{mock_data.mock_cls}({"return_value" if mock_data.return_value else "side_effect"}' \
                   f'={mock_arg_var_name})\n'
        # decorator: str = f'@mock.patch({mock_data.target}, {mock_var_name})'
        file.writelines([mock_arg, mock_obj])
        return mock_arg_var_name, mock_var_name


class TestGenerator:
    @staticmethod
    def generate_test_endpoint(path: str):
        with open(path, 'r') as readable_file, open('../../autotests/mock_data.py', 'w+') as writable_file:
            data = json.load(readable_file)
            for obj in data:
                MockGenerator.generate_mock(obj, writable_file)


if __name__ == '__main__':
    TestGenerator.generate_test_endpoint('./file.json')
