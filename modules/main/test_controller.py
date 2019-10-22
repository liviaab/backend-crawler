import pytest
import modules.main.controller as controller
import modules.db.database as db
import tests.fixtures.process_formatted as process_formatted
import tests.fixtures.process_json as process_json

class ObjectView(object):
    def __init__(self, d):
        self.__dict__ = d

def test__get_courts(monkeypatch):
    def mock_function():
        return None

    def mock_open():
        obj = ObjectView({ 'close': mock_function })
        return obj

    def mock_get_courts(conn):
        return process_formatted.courts_fixture()

    monkeypatch.setattr(db, "open", mock_open)
    monkeypatch.setattr(db, "get_courts", mock_get_courts)
    result = controller.get_courts()

    assert result[0]['id'] == 1
    assert result[0]['name'] == 'Tribunal de Justiça do Estado de Alagoas'
    assert result[0]['initials'] == 'TJAL'


def test__get_process_info_in_database(monkeypatch):
    json = process_json.process_info()

    def mock_function():
        return None

    def mock_open():
        obj = ObjectView({ 'close': mock_function })
        return obj

    def mock_get_process(conn, process_number):
        info = process_json.process_info()
        members = process_formatted.members()
        changes = process_formatted.changes()
        return (info, members, changes)

    def mock_process_info_to_json(info, parties_involved, movimentations):
        return json

    monkeypatch.setattr(db, "open", mock_open)
    monkeypatch.setattr(db, "get_process", mock_get_process)
    monkeypatch.setattr(controller, "__process_info_to_json", mock_process_info_to_json)
    result = controller.get_process_info('12345')

    assert result == json
