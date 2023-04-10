from . import PhoneBook
from . import get_path
import json

ENCODING = 'UTF-8'


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, PhoneBook):
            return {f'__{o.__class__.__name__}__': o.__dict__}
        elif isinstance(o, PhoneBook.Contact):
            return {f'__{o.__class__.__name__}__': o.__dict__}
        return {f'__{o.__class__.__name__}__': o.__dict__}


def decode(entity):
    if (key := f'__{PhoneBook.__name__}__') in entity:
        return PhoneBook().__dict__.update(entity[key])
    elif (key := f'__{PhoneBook.Contact.__name__}__') in entity:
        return PhoneBook.Contact().__dict__.update(entity[key])
    return entity


def serialization(entity, path: str = str(), encoding: str = ENCODING) -> None:
    path = path if path else get_path()
    with open(path, 'w', encoding=encoding) as file:
        json.dump(entity, file, ensure_ascii=False, cls=CustomEncoder, allow_nan=False)


def deserialization(path: str = str(), encoding: str = ENCODING) -> list:
    path = path if path else get_path()
    with open(path, 'r', encoding=encoding) as file:
        data = json.load(file, object_hook=decode)
    return data
