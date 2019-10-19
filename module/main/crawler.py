import requests

PROCESS_NUMBER_LENGTH = 25
UNIFIED_DIGIT_AND_YEAR_INDEX = 15
UNIFIED_FORUM_INDEX = 21

default_payload = {
    'conversationId': '',
    'dadosConsulta.localPesquisa.cdLocal': '-1',
    'cbPesquisa': 'NUMPROC',
    'dadosConsulta.tipoNuProcesso': 'UNIFICADO',
    'dadosConsulta.valorConsulta': '',
    'uuidCaptcha':''
}


class CourtCrawler:
    def __init__(self, base_url='https://www2.tjal.jus.br/cpopg/search.do',
                payload=default_payload):
        self.base_url = base_url
        self.payload = payload

    def _set_payload_process_number(self, process_number):
        if len(process_number) != PROCESS_NUMBER_LENGTH:
            raise ValueError('The process number does not have the correct format.\nIt must have 25 characters.\n')

        self.payload['numeroDigitoAnoUnificado'] = process_number[:UNIFIED_DIGIT_AND_YEAR_INDEX]
        self.payload['foroNumeroUnificado'] = process_number[UNIFIED_FORUM_INDEX:]
        self.payload['dadosConsulta.valorConsultaNuUnificado'] = process_number

    def get_process(self, process_number):
        self._set_payload_process_number(process_number)
        response = requests.get(self.base_url, params=self.payload)
        return response.status_code, response.text
