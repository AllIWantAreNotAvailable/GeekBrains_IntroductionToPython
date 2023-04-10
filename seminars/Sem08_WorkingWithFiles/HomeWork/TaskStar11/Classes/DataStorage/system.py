import os


def get_path(data_dir: str = 'data', data_file: str = 'data.json', mode='w', encoding: str = 'UTF-8') -> str:
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)
    if not os.path.exists(path := os.path.join(data_dir, data_file)):
        with open(path, mode, encoding=encoding):
            pass
    return path
