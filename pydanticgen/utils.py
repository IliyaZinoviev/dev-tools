import re
from itertools import chain
from typing import Optional, Match, AnyStr


def is_camel(some_str: str) -> Optional[Match[AnyStr]]:
    return re.search(r'^[a-z]+(?:[A-Z][a-z]+)*$', some_str)


def is_snake(some_str: str) -> Optional[Match[AnyStr]]:
    return re.search(r'^[a-z]+(?:_[a-z]+)*$', some_str)


def convert2snake(some_str: str):
    some_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', some_str)
    some_str = re.sub('__([A-Z])', r'_\1', some_str)
    some_str = re.sub('([a-z0-9])([A-Z])', r'\1_\2', some_str)
    return some_str.lower()


def convert2camel(snake_str: str):
    seps: list[str] = ['_', '-']
    others = multiple_split(snake_str, *seps)
    return ''.join(map(str.title, others))


def multiple_split(some_str: str, *seps) -> list[str]:
    strings: list[str] = [some_str]
    for sep in seps:
        strings_matrix: list[list[str]] = [s.split(sep) for s in strings]
        strings: list[str] = list(chain(*strings_matrix))
    return strings