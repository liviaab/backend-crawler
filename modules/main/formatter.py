from bs4 import BeautifulSoup

def parseHTML(text):
    return BeautifulSoup(text, 'html.parser')

def find_process_info(parsed_doc):
    [_, process_info] = parsed_doc.find_all('table', class_='secaoFormBody')
    process_info_formatted = __strip_text_data(process_info)
    return __keyword_list_to_dict(process_info_formatted)

def find_parties_involved(parsed_doc):
    parties_involved = parsed_doc.find(id='tablePartesPrincipais')
    parties_involved_formatted = __strip_text_data(parties_involved)
    return __keyword_list_to_dict(parties_involved_formatted)

def find_changes(parsed_doc):
    last_changes = parsed_doc.find(id='tabelaUltimasMovimentacoes').find_all('tr')
    return __changes_list(last_changes)


def __strip_text_data(data):
    return [text for text in data.stripped_strings]

def __keyword_list_to_dict(list):
    return  {list[i]: list[i+1] for i in range(0, len(list)) if list[i].endswith(':')}

def __changes_list(list):
    return [__strip_text_data(item) for item in list]
