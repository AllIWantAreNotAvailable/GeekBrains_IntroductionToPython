from . import serialize
from . import deserialize
from . import Logger, DEBUG

LOGGER = Logger(logger_name='PhoneBook',
                dir_name='logs',
                log_file_name='logs.log',
                level=DEBUG)


class PhoneBook:
    """ Класс представляет собой справочник контактов.
    """

    def __init__(self, phonebook: list = None) -> None:
        LOGGER.logger.debug(f'Начато создание экземпляра: {id(self)}; класса "{PhoneBook.__name__}".')
        self.entries = phonebook if isinstance(phonebook, list) and phonebook else list()
        LOGGER.logger.debug(f'Создан экземпляра: {id(self)}; класса "{PhoneBook.__name__}".\n'
                            f'\tЗначение атрибута "entries": {self.entries }')

    def __len__(self):
        return len(self.entries)

    def __getitem__(self, key):
        return self.entries[key]

    def __setitem__(self, key, value):
        self.entries[key] = value

    def __delitem__(self, key):
        del self.entries[key]

    def __iter__(self):
        return iter(self.entries)

    def __reversed__(self):
        return reversed(self.entries)

    def __str__(self):
        return '\n\n'.join(map(str, self.entries))

    def load(self):
        self.entries = deserialize()

    def save(self):
        serialize(self)

    def create(self, **kwargs) -> None:
        self.entries.append(self.Contact(**kwargs))

    def edit_contact(self):
        pass

    def delete(self):
        pass

    def find(self):
        pass

    class Contact:
        """ Класс представляет собой запись в справочнике контактов.
        """

        def __init__(self, first_name: str = None, second_name: str = None, surname: str = None):
            self.entity = {
                'Имя': first_name if first_name else str(),
                'Фамилия': second_name if second_name else str()
            }
            if surname:
                self.entity['Отчество'] = surname

        def __len__(self):
            return len(self.entity)

        def __getattr__(self, item):
            return self.entity[item]

        def __setattr__(self, key, value):
            self.entity[key] = value

        def __delitem__(self, key):
            del self.entity[key]

        def __iter__(self):
            return iter(self.entity)

        def __str__(self):
            contact = list()
            full_name = f'Контакт id={id(self)}: ' \
                        f'{self.entity["Фамилия"]} {self.entity["Имя"]}' \
                        f'{" " + self.entity["Отчество"] if "Отчество" in self.entity else ""}'
            contact.append(full_name)
            return '\n\t'.join(f'{element}' for element in contact)
