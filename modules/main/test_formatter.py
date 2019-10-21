import modules.main.formatter as formatter
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
    expected_object = \
        {
            'Processo:': '0067154-55.2010.8.02.0001 (001.10.067154-4)',
            'Classe:': 'Ação Civil Pública',
            'Área:': 'Cível',
            'Assunto:': 'Tratamento Médico-Hospitalar e/ou Fornecimento de Medicamentos',
            'Distribuição:': '29/09/2010 às 15:57 - Sorteio',
            'Controle:': '2010/001061/td>',
            'Juiz:': 'Geraldo Tenório Silveira Júnior',
            'Valor da ação:': 'R$ 510,00'
        }

    assert formatter.find_process_info(html_parsed) == expected_object


def test_find_parties_involved(html_parsed):
    expected_object =\
        {
            'Autor:': "' de Alagoas",
            'Defensor P:': 'Sabrina da Silva Cerqueira Dattoli',
            'Réu:': 'Município de Maceió',
            'Procurador:': 'Procurador Geral do Município'
        }

    assert formatter.find_parties_involved(html_parsed) == expected_object


def test_find_changes(html_parsed):
    expected_object =\
        [
            ['15/09/2017', 'Baixa Definitiva'],
            ['05/07/2016', 'Determinada Requisição de Informações', "Processo n° 0067154-55.2010.8.02.0001 Ação: Ação Civil Pública Autor: ''Defensoria Publica do Estado de AlagoasRéu: Município de Maceió DESPACHOAo cartório para verificar prazo para interposição de recurso.Havendo trânsito em julgado, arquivem-se os autos com baixa na distribuição.Maceió, 05 de julho de 2016.Antonio Emanuel Dória Ferreira Juiz de Direito"],
            ['11/07/2014', 'Conclusos'],
            ['11/07/2014', 'Juntada de Documento'],
            ['11/07/2014', 'Juntada de Documento']
        ]
    assert formatter.find_changes(html_parsed) == expected_object
