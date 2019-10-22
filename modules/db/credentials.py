import os

ROOT_DIR = os.path.abspath(__file__ + '../../../../')


def build():
    return __local_credentials()

def __local_credentials():
    return __read_credentials('db_credentials.local')


def __read_credentials(file_name):
    file_path = os.path.join(ROOT_DIR, 'configs/' + file_name)

    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            credentials[key] = value

    return credentials
