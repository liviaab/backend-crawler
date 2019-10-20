import json
from datetime import datetime, timedelta
import modules.db.database as db
from modules.main import crawler as cw, formatter

def get_courts():
    conn = db.open()
    results = db.get_courts(conn)
    db.close(conn)
    return results

def get_process_info(process_number):
    info = None
    parties_involved = []
    movimentations = []
    conn = db.open()
    result = db.get_process(conn, process_number)

    if(result == None):
        details, entities, changes = __make_request(process_number)
        db.insert_process(conn, details, entities, changes)
        info, parties_involved, movimentations = db.get_process(conn, process_number)
        db.close(conn)
        return __process_complete_info_to_json(info, parties_involved, movimentations)

    info, parties_involved, movimentations = result

    if(__last_access_greater_than_a_day(info['last_access'])):
        process_id = info['id']
        details, entities, changes = __make_request(process_number)
        db.update_process(conn, process_id, details, entities, changes)
        info, parties_involved, movimentations = db.get_process(conn, process_number)

    db.close(conn)
    return __process_complete_info_to_json(info, parties_involved, movimentations)


def __parse_data(text):
    parsed_data = formatter.parseHTML(text)
    process_info = formatter.find_process_info(parsed_data)
    parties_involved = formatter.find_parties_involved(parsed_data)
    changes = formatter.find_changes(parsed_data)
    return process_info, parties_involved, changes

def __make_request(process_number):
    crawler = cw.CourtCrawler()
    status, html_text = crawler.get_process(process_number)
    return __parse_data(html_text)

def __last_access_greater_than_a_day(date):
    DAY_IN_SECONDS = 24*60*60
    delta = datetime.now() - date
    return delta.seconds > DAY_IN_SECONDS

def __process_complete_info_to_json(info, parties_involved, movimentations):
    complete_info = {key: info[key] for key in info}
    complete_info['last_access'] = str(complete_info['last_access'].strftime("%d/%m/%y"))
    complete_info['parties_involved'] = []
    complete_info['movimentations'] = []

    for entity in parties_involved:
        complete_info['parties_involved'].append({key: entity[key] for key in entity})

    for change in movimentations:
        complete_info['movimentations'].append({key: change[key] for key in change})

    return json.loads(json.dumps(complete_info))
