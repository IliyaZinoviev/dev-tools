from abc import ABC, abstractmethod


class BaseFactory(ABC):

    def __init__(self, *_, **__):
        self._next_id = 0
        self.obj_dict = {}

    @abstractmethod
    def _create(self, id_val: int, *args, **kw) -> object:
        """ Method is designed for creating object"""

    def get_or_create(
            self,
            id_val: int = None,
            *args,
            **kw,
    ) -> object:
        while not id_val:
            if self._next_id not in self.obj_dict:
                id_val = self._next_id
            self._next_id += 1

        if id_val in self.obj_dict:
            return self.obj_dict[id_val]

        obj = self._create(id_val, *args, **kw)
        self.obj_dict[id_val] = obj
        return obj

    def set_counter(self, count):
        self._next_id = count

    def reset_counter(self):
        self._next_id = 0

    @staticmethod
    def _data_factory(fields_names, default_obj, **kw):
        return default_obj | {k: v for k, v in kw.items() if k in fields_names}
