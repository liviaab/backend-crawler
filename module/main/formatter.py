from bs4 import BeautifulSoup

def parseHTML(text_response):
    return BeautifulSoup(response.text, 'html.parser')

def find_process_info(parsed_doc):
    [_, process_info] = soup.find_all('table', class_='secaoFormBody')
    process_info_formatted = __strip_text_data(process_info)
    return __keyword_list_to_dict(process_info_formatted)

def find_parties_involved(parsed_doc):
    parties_involved = parsed_doc.find(id='tablePartesPrincipais')
    parties_involved_formatted = __strip_text_data(parties_involved)
    return __keyword_list_to_dict(parties_involved)

def find_changes(parsed_doc):
    last_changes = parsed_doc.find(id='tabelaUltimasMovimentacoes').find_all('tr')
    return __changes_list_to_dict(last_changes)



def __strip_text_data(data):
    return [text for text in data.stripped_strings]

def __keyword_list_to_dict(list):
    return  { list[i]: list[i+1] for i in range(0, len(list)) if list[i].endswith(':') }

def __changes_list_to_dict(list):
    changes = {}
    DATE_INDEX = 0
    MOVES_INDEX = 1

    for change in list:
        moves =  __strip_text_data(change)
        date = moves[DATE_INDEX]
        changes[date] = moves[MOVES_INDEX:]
