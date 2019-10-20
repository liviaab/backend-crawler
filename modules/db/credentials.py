import os

ROOT_DIR = os.path.abspath(__file__ + '../../../../')


def build():
    file_path = os.path.join(ROOT_DIR, 'configs/db_credentials.ini')
    credentials = {}

    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            credentials[key] = value

    return credentials
