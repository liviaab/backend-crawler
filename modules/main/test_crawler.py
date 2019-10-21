import pytest
import re
from modules.main.crawler import CourtCrawler


TEST_BASE_URL = 'http://base.url/api/v1/'
PROCESS_NUMBER = '0067154-55.2010.8.02.0001'
match_url = re.compile('^' + TEST_BASE_URL)
crawler = CourtCrawler(base_url=TEST_BASE_URL)


def test__get_process(requests_mock):
    requests_mock.get(match_url, text="Pretty Fly")
    status, text = crawler.get_process(PROCESS_NUMBER)

    assert text == "Pretty Fly"
    assert status == 200


def test__get_process_raises_error(requests_mock):
    requests_mock.get(match_url, text="Pretty Fly")
    # crawler = CourtCrawler(base_url=TEST_BASE_URL)

    with pytest.raises(ValueError) as error:
        crawler.get_process('13245')
        print(error)

    assert str(error.value) == 'The process number does not have the correct format.\nIt must have 25 characters.\n'

