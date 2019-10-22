from datetime import datetime

def process_info():
    process = \
    {
        "id": 1,
        "process_number": "0067154-55.2010.8.02.0001",
        "process_class": "Ação Civil Pública",
        "area": "Cível",
        "subject": "Tratamento Médico-Hospitalar e/ou Fornecimento de Medicamentos",
        "distribution_date": "29/09/2010 às 15:57 - Sorteio",
        "judge": "Geraldo Tenório Silveira Júnior",
        "value": "R$         510,00",
        "last_access": datetime.now().strftime("%d/%m/%y"),
        "court_id": 1,
        "parties_involved": [
            {
                "id": 25,
                "process_id": 1,
                "name": "' de Alagoas",
                "role": "Autor"
            },
            {
                "id": 26,
                "process_id": 1,
                "name": "Sabrina da Silva Cerqueira Dattoli",
                "role": "Defensor P"
            },
            {
                "id": 27,
                "process_id": 1,
                "name": "Município de Maceió",
                "role": "Réu"
            },
            {
                "id": 28,
                "process_id": 1,
                "name": "Procurador Geral do Município",
                "role": "Procurador"
            }
        ],
        "movimentations": [
            {
                "id": 26,
                "process_id": 1,
                "date": "15/09/2017",
                "description": "Baixa Definitiva"
            },
            {
                "id": 27,
                "process_id": 1,
                "date": "05/07/2016",
                "description": "Determinada Requisição de Informações\nProcesso n° 0067154-55.2010.8.02.0001 Ação: Ação Civil Pública Autor: ''Defensoria Publica do Estado de AlagoasRéu: Município de Maceió DESPACHOAo cartório para verificar prazo para interposição de recurso.Havendo trânsito em julgado, arquivem-se os autos com baixa na distribuição.Maceió, 05 de julho de 2016.Antonio Emanuel Dória Ferreira Juiz de Direito"
            },
            {
                "id": 28,
                "process_id": 1,
                "date": "11/07/2014",
                "description": "Conclusos"
            },
            {
                "id": 29,
                "process_id": 1,
                "date": "11/07/2014",
                "description": "Juntada de Documento"
            },
            {
                "id": 30,
                "process_id": 1,
                "date": "11/07/2014",
                "description": "Juntada de Documento"
            }
        ]
    }

    return process
