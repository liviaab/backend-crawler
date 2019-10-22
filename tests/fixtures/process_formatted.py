def courts_fixture():
    courts = \
    [
        {
            "id": 1,
            "name": "Tribunal de Justiça do Estado de Alagoas",
            "initials": "TJAL"
        }
    ]
    return courts

def obj_info():
    info = \
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
    return info


def obj_parties():
    parties = \
        {
            'Autor:': "' de Alagoas",
            'Defensor P:': 'Sabrina da Silva Cerqueira Dattoli',
            'Réu:': 'Município de Maceió',
            'Procurador:': 'Procurador Geral do Município'
        }
    return parties


def obj_changes():
    changes = \
        [
            ['15/09/2017', 'Baixa Definitiva'],
            ['05/07/2016', 'Determinada Requisição de Informações', "Processo n° 0067154-55.2010.8.02.0001 Ação: Ação Civil Pública Autor: ''Defensoria Publica do Estado de AlagoasRéu: Município de Maceió DESPACHOAo cartório para verificar prazo para interposição de recurso.Havendo trânsito em julgado, arquivem-se os autos com baixa na distribuição.Maceió, 05 de julho de 2016.Antonio Emanuel Dória Ferreira Juiz de Direito"],
            ['11/07/2014', 'Conclusos'],
            ['11/07/2014', 'Juntada de Documento'],
            ['11/07/2014', 'Juntada de Documento']
        ]

    return changes
