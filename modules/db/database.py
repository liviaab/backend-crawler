import mysql.connector as db
from datetime import datetime
import modules.db.credentials as credentials


DEFAULT_COURT_ID = 1
ID_INDEX = 1


def open():
    params = credentials.build()
    conn = None

    try:
        conn = db.connect(
          host=params['host'],
          user=params['user'],
          passwd=params['password'],
          database=params['database']
        )
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
    cursor = conn.cursor(dictionary=True)
    return __execute_query__(cursor, query, None)


def get_process(conn, process_number):
    cursor = conn.cursor(dictionary=True)
    try:
        info = __select_process(cursor, process_number)

        if(info is None):
            return None

        parties_involved = __select_parties_involved(cursor, info['id'])
        movimentations = __select_movimentations(cursor, info['id'])

        return info, parties_involved, movimentations
    except Exception as error:
        print(error)


def insert_process(conn, process_info, entities, changes):
    try:
        cursor = conn.cursor()
        __insert_into_process(cursor, process_info)
        conn.commit()
        process_id = cursor.lastrowid
        __insert_into_parties_involved(cursor, process_id, entities)
        __insert_into_movimentations(cursor, process_id, changes)
        conn.commit()
        cursor.close()
    except Exception as error:
        print(error)


def update_process(conn, process_id, details, entities, changes):
    try:
        cursor = conn.cursor()
        __update_process(cursor, process_id, details)
        __update_parties_involved(cursor, process_id, entities)
        __update_movimentations(cursor, process_id, changes)
        conn.commit()
    except (Exception) as error:
        print(error)


def __execute_query__(cursor, query, data):
    try:
        cursor.execute(query, data)
        return cursor.fetchall()
    except (Exception) as error:
        print(error)


def __select_process(cursor, process_number):
    query = 'SELECT * FROM processes WHERE processes.process_number = %s;'
    info = __execute_query__(cursor, query, (process_number,))
    if(info is None or info == []):
        return None

    [single_info] = info
    return single_info


def __select_parties_involved(cursor, process_id):
    query = 'SELECT pi.* FROM parties_involved as pi '\
            'LEFT JOIN processes as p '\
            'ON pi.process_id = p.id AND p.id = %s;'
    return __execute_query__(cursor, query, (process_id,))


def __select_movimentations(cursor, process_id):
    query = 'SELECT m.* FROM movimentations as m '\
            'LEFT JOIN processes as p '\
            'ON m.process_id = p.id AND p.id = %s;'
    return __execute_query__(cursor, query, (process_id,))


def __format_process_info(info):
    insert_values = (info['Processo:'], info['Classe:'], info['Área:'],
                     info['Assunto:'], info['Distribuição:'], info['Juiz:'],
                     info['Valor da ação:'], datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                     DEFAULT_COURT_ID)
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
            'subject, distribution_date, judge, value, last_access, court_id) '\
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);'
    values = __format_process_info(process_info)
    return cursor.execute(query, values)


def __insert_into_movimentations(cursor, process_id, changes):
    query = 'INSERT INTO movimentations(process_id, date, description) '\
            'VALUES (%s, %s, %s);'
    values = __format_process_movimentations(process_id, changes)
    return cursor.executemany(query, values)


def __insert_into_parties_involved(cursor, process_id, parties_involved):
    query = 'INSERT INTO parties_involved(process_id, name, role) VALUES (%s, %s, %s);'
    values = __format_parties_values(process_id, parties_involved)
    return cursor.executemany(query, values)


def __update_process(cursor, process_id, details):
    query_info = 'UPDATE processes SET process_class = %s, area = %s, '\
                 'subject = %s, distribution_date = %s, judge = %s, value = %s, '\
                 'last_access = %s WHERE processes.id = %s ;'
    values = __format_process_info(details)
    values_to_update = list(values[1:-1])
    values_to_update.append(process_id)
    return cursor.execute(query_info, tuple(values_to_update))


def __update_parties_involved(cursor, process_id, entities):
    query = 'DELETE FROM parties_involved WHERE process_id = %s;'
    cursor.execute(query, (process_id,))
    __insert_into_parties_involved(cursor, process_id, entities)


def __update_movimentations(cursor, process_id, changes):
    query = 'DELETE FROM movimentations WHERE process_id = %s;'
    cursor.execute(query, (process_id,))
    __insert_into_movimentations(cursor, process_id, changes)
