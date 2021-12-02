from typing import Any


def call_multiple_assert(*args: tuple[str, Any]):
    for name, item in args:
        assert item, f'Value of {name} param are required!!!'