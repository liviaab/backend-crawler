import psycopg2 as pg
from psycopg2.extras import RealDictCursor, execute_values, Json
from psycopg2.extensions import register_adapter
from datetime import datetime
import modules.db.credentials as credentials


register_adapter(dict, Json)
DEFAULT_COURT_ID = 1
ID_INDEX = 1


def open():
    params = credentials.build()
    conn = None

    try:
        conn = pg.connect(**params)
        return conn
    except Exception as error:
        print(error)
        if conn is not None:
            conn.close()


def close(conn):
    if conn is not None:
        conn.close()


def get_courts(conn):
    query = 'SELECT * FROM courts;'
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    return __execute_query__(cursor, query, None)


def get_process(conn, process_number):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    try:
        info = __select_process(cursor, process_number)
        parties_involved = __select_parties_involved(cursor, process_number)
        movimentations = __select_movimentations(cursor, process_number)
        return info, parties_involved, movimentations
    except Exception as error:
        print(error)


def insert_process(conn, process_info, entities, changes):
    try:
        cursor = conn.cursor()
        process_id = __insert_into_process(cursor, process_info)
        __insert_into_parties_involved(cursor, process_id, entities)
        __insert_into_movimentations(cursor, process_id, changes)
        conn.commit()
    except Exception as error:
        print(error)


def update_process(conn, process_id, details, entities, changes):
    try:
        cursor = conn.cursor()
        __update_process(cursor, process_id, details)
        __update_parties_involved(cursor, process_id, entities)
        __update_movimentations(cursor, process_id, changes)
        conn.commit()
    except (Exception, pg.DatabaseError) as error:
        print(error)


def __execute_query__(cursor, query, data):
    try:
        cursor.execute(query, data)
        return cursor.fetchall()
    except (Exception, pg.DatabaseError) as error:
        print(error)


def __select_process(cursor, process_number):
    query = 'SELECT * FROM processes WHERE processes.process_number = %s;'
    info = __execute_query__(cursor, query, (process_number,))
    if(info is None or info == []):
        return None

    [single_info] = info
    return single_info


def __select_parties_involved(cursor, process_number):
    query = 'SELECT pi.* FROM parties_involved as pi '\
            'LEFT JOIN processes as p '\
            'ON pi.process_id = p.id AND p.process_number = %s;'
    return __execute_query__(cursor, query, (process_number,))


def __select_movimentations(cursor, process_number):
    query = 'SELECT m.* FROM movimentations as m '\
            'LEFT JOIN processes as p '\
            'ON m.process_id = p.id AND p.process_number = %s;'
    return __execute_query__(cursor, query, (process_number,))


def __format_process_info(info):
    insert_values = (info['Processo:'], info['Classe:'], info['Área:'],
                     info['Assunto:'], info['Distribuição:'], info['Juiz:'],
                     info['Valor da ação:'], datetime.now(), DEFAULT_COURT_ID)
    return insert_values


def __format_process_movimentations(process_id, changes):
    values = []
    for item in changes:
        date = item[0]
        descriptions = "\n".join(item[1:])
        values.append((process_id, date, descriptions))
    return values


def __format_parties_values(process_id, parties_involved):
    values = []
    for (role, name) in parties_involved.items():
        values.append((process_id, name, role.strip(':')))
    return values


def __insert_into_process(cursor, process_info):
    query = 'INSERT INTO processes(process_number, process_class, area, '\
            'subject, distribution_date, judge, value, last_access, court_id)'\
            ' VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *;'
    values = __format_process_info(process_info)
    cursor.execute(query, values)
    row = cursor.fetchone()

    process_id = row[0]
    return process_id


def __insert_into_movimentations(cursor, process_id, changes):
    query = 'INSERT INTO movimentations(process_id, date, description) '\
            'VALUES %s;'
    values = __format_process_movimentations(process_id, changes)
    execute_values(cursor, query, values)


def __insert_into_parties_involved(cursor, process_id, parties_involved):
    query = 'INSERT INTO parties_involved(process_id, name, role) VALUES %s;'
    values = __format_parties_values(process_id, parties_involved)
    execute_values(cursor, query, values)


def __update_process(cursor, process_id, details):
    query_info = 'UPDATE processes SET (process_class, area, subject, '\
                 'distribution_date, judge, value, last_access) = %s'\
                 'WHERE processes.id = %s ;'
    values = __format_process_info(details)
    values_to_update = values[1:-1]
    cursor.execute(query_info, (values_to_update, process_id))


def __update_parties_involved(cursor, process_id, entities):
    query = 'DELETE FROM parties_involved WHERE process_id = %s;'
    cursor.execute(query, (process_id,))
    __insert_into_parties_involved(cursor, process_id, entities)


def __update_movimentations(cursor, process_id, changes):
    query = 'DELETE FROM movimentations WHERE process_id = %s;'
    cursor.execute(query, (process_id,))
    __insert_into_movimentations(cursor, process_id, changes)
