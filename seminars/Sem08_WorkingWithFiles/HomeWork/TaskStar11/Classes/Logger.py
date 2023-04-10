__all__ = ['Logger', 'NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']

from . import get_path
import logging

NOTSET = logging.NOTSET
DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL


class Logger:
    def __init__(self,
                 logger_name: str,
                 dir_name: str,
                 log_file_name: str,
                 path: str = str(),
                 level: int = NOTSET,
                 encoding: str = 'UTF-8',
                 str_format: str = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s',
                 datestamp_format: str = '%Y-%m-%d %H:%M:%S'):

        # Уровень логирования
        self.level = level

        # Инициализируем регистратор
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(self.level)

        # Инициализируем обработчик записи логирования
        path = path if path else get_path(data_dir=dir_name,
                                          data_file=log_file_name,
                                          mode='a+',
                                          encoding=encoding
                                          )
        self.handler = logging.FileHandler(path)
        self.handler.setLevel(self.level)
        self.handler.encoding = encoding

        # Устанавливаем шаблон ведения логов
        self.formatter = logging.Formatter(fmt=str_format, datefmt=datestamp_format)

        # Добавляем шаблон обработчику записи логирования
        self.handler.setFormatter(self.formatter)

        # Добавляем обработчик записи логирования регистратору
        self.logger.addHandler(self.handler)
