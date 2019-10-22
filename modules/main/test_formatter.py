import modules.main.formatter as formatter
import tests.fixtures.process_formatted as process_formatted
import os
import pytest


ROOT_DIR = os.path.abspath(__file__ + '../../../../')


def test_parseHTML():
    assert str(formatter.parseHTML('<p>Lívia &</p>')) == "<p>Lívia &amp;</p>"


@pytest.fixture
def html_parsed():
    file_content = []
    file_path = os.path.join(ROOT_DIR, 'tests/fixtures/process.html')

    with open(file_path, 'r') as file:
        file_content = formatter.parseHTML(file)

    return file_content


def test_find_process_info(html_parsed):
    expected_object = process_formatted.info()

    assert formatter.find_process_info(html_parsed) == expected_object


def test_find_parties_involved(html_parsed):
    expected_object = process_formatted.members()

    assert formatter.find_parties_involved(html_parsed) == expected_object


def test_find_changes(html_parsed):
    expected_object = process_formatted.changes()
    assert formatter.find_changes(html_parsed) == expected_object
