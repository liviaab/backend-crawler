import json
from datetime import datetime
import modules.db.database as db
from modules.main import crawler as cw, formatter
import flask_restful


PROCESS_NUMBER_LENGTH = 25


def get_courts():
    conn = db.open()
    results = db.get_courts(conn)
    db.close(conn)
    return results


def get_process_info(process_number):
    if( not __is_valid_process_number(process_number)):
        flask_restful.abort(400)
        return

    info = None
    members = []
    movimentations = []
    conn = db.open()
    result = db.get_process(conn, process_number)

    if(result is None):
        details, entities, changes = __make_request(process_number)
        db.insert_process(conn, details, entities, changes)
        info, members, movimentations = db.get_process(conn, process_number)
        db.close(conn)
        return __process_info_to_json(info, members, movimentations)

    info, members, movimentations = result

    if(__last_access_greater_than_a_day(info['last_access'])):
        process_id = info['id']
        details, entities, changes = __make_request(process_number)
        db.update_process(conn, process_id, details, entities, changes)
        info, members, movimentations = db.get_process(conn, process_number)

    db.close(conn)
    return __process_info_to_json(info, members, movimentations)


def __is_valid_process_number(process_number):
    return len(process_number) == PROCESS_NUMBER_LENGTH


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
    if(isinstance(date, str)):
        date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')

    DAY_IN_SECONDS = 24 * 60 * 60
    delta = datetime.now() - date
    return delta.seconds > DAY_IN_SECONDS


def __process_info_to_json(info, parties_involved, movimentations):
    process = {key: info[key] for key in info}
    process['last_access'] = str(process['last_access'])
    process['parties_involved'] = []
    process['movimentations'] = []

    for entity in parties_involved:
        process['parties_involved'].append(
            {key: entity[key] for key in entity}
        )

    for change in movimentations:
        process['movimentations'].append({key: change[key] for key in change})

    return json.loads(json.dumps(process))
