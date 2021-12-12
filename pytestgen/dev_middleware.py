import inspect
import json
import re
import types
from contextvars import ContextVar
from enum import Enum
from functools import wraps
from typing import Iterable, Any, Optional

from pydantic import BaseModel
from starlette.requests import Request
from starlette.routing import Route

mock_data = ContextVar('mock_data', default={})


def filter_routes_by_tags(tags: set[str], routes: list[Route]) -> Iterable[Route]:
    return filter(lambda r: hasattr(r, 'tags') and tags.intersection(r.tags), routes)


async def handle_mock_data_middleware(routes: list[Route], tags: set[str], request: Request, call_next):
    response = await call_next(request)
    for route in filter_routes_by_tags(tags, routes):
        if re.search(route.path_regex, request.url.path):
            path = request.url.path[1:].replace('/', '_')
            with open(f'{path}.json', 'w') as file:
                json.dump(list(mock_data.get().values()), file, ensure_ascii=False, indent=4)
    mock_data.set({})
    return response


# def put_output_mock_data(key):
#     def decorator(fn):
#         @wraps(fn)
#         async def wrap(*args, **kw):
#             res: BaseModel = await fn(*args, **kw)
#             mock_data.get().append((key, res.__class__.__name__, res.dict()))
#             return res
#         return wrap
#     return decorator


# def put_input_output_to_mock_data_sync(import_path_to_mocked_fn):
#     def decorator(fn):
#         @wraps(fn)
#         def wrap(*args, **kw):
#             res = fn(*args, **kw)
#             res_id = id(res)
#             mock_data.get()[res_id] = [fn.__name__, (args, kw), res]
#             return res
#         return wrap
#     return decorator


# ResponseDataMethodName: TypeAlias = str


# def apply_put_mock_data_decorator_to_methods(method_dict: dict[object, list[ResponseDataMethodName]]):
#     for cls in method_dict.keys():
#         public_method_names = method_dict[cls]
#         for name in public_method_names:
#             attr = getattr(cls, name)
#             setattr(cls, name, put_output_mock_data(name)(attr))


class ResultProxy:

    def __init__(self, obj):
        self.res = obj
        self.res_id = id(obj)
        self.side_effect_item_dict: dict = {}

    def __getattr__(self, item):
        attr = getattr(self.res, item)
        if isinstance(attr, types.MethodType):
            val = attr()
        else:
            val = attr
        self.side_effect_item_dict[item] = val
        return attr


class ResponseProxy(ResultProxy):

    def __init__(self, obj, mock_data_key):
        super().__init__(obj)
        self.mock_data_key = mock_data_key

    def __del__(self):
        mock_data_dict = mock_data.get()
        mock_data_dict[self.mock_data_key]['side_effect'].append(self.side_effect_item)


def put_input_output_to_mock_data_sync(import_path_to_mocked_fn: str = None):
    def decorator(fn):
        @wraps(fn)
        def wrap(*args, **kw):
            res = fn(*args, **kw)
            mock_data_dict = mock_data.get()
            res_id = id(res)
            mock_data_dict[res_id] = {
                'target': import_path_to_mocked_fn,
                'mock_cls': MockClassEnum.Mock,
                'return_value': res,
                'input_data': (args, kw),
                'mocked_obj_var_name': fn.__name__,
            }
            return res

        return wrap

    return decorator


# def put_input_output_to_mock_data_async(import_path_to_mocked_fn: str = None, name: str = None):
#     def decorator(fn):
#         @wraps(fn)
#         async def wrap(*args, **kw):
#             res = await fn(*args, **kw)
#             mock_data_dict = mock_data.get()
#             res_id = id(res)
#             proxy = ResultProxy(res)
#             mock_data_dict[res_id] = [import_path_to_mocked_fn, 'AsyncMock', name, (args, kw)]
#             return proxy
#         return wrap
#     return decorator



class MockDataApiCall:
# class MockDataApiCall(SomeClass):
    async def _call(self, parameters: dict) -> ResultProxy:
        res = await super()._call(parameters)
        mock_data_dict = mock_data.get()
        res_id = id(res)
        proxy = ResultProxy(res)
        frame_info = inspect.stack()[
            inspect.stack().index(list(filter(lambda x: x.function == '__call__', inspect.stack()))[0]) + 1]
        # import_path_to_obj_attr = frame_info.filename[frame_info.filename.find(config.APP_NAME.replace('-', '_')):-3].replace('/', '.')
        # api_call_name = re.findall(r'\.(?P<api_call_name>\w+)\(', frame_info.code_context[0])[0]
        target = 'httpx_apicall_target'
        mock_data_dict[target] = {
            'target': target,
            'mock_cls': MockClassEnum.AsyncMock,
            'side_effect': [],
            'input_data': parameters,
            'mocked_obj_var_name': self._method + self._path.replace('/', '-'),
        }
        return proxy


class MockSchema(BaseModel):
    return_value: Optional[Any]
    side_effect: Optional[list[dict]]
    mock_cls: str
    input_data: Optional[Any]
    mocked_obj_var_name: str
    target: Optional[str]


class TestViewData(BaseModel):
    path: str
    name: str
    params: dict
    headers: dict
    mock_data: list[MockSchema]


class MockClassEnum(str, Enum):
    Mock = 'Mock'
    AsyncMock = 'AsyncMock'
