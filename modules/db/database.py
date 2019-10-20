import psycopg2 as pg
from psycopg2.extras import RealDictCursor
import modules.db.credentials as credentials

def __execute_query__(conn, query):
    try:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pg.ProgrammingError as error:
        print(error)
        return None
    except (Exception, pg.DatabaseError) as error:
        print(error)


def open():
    params = credentials.build()
    conn = None

    try:
        print(params)
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
    return __execute_query__(conn, query)

def get_process(conn, process_number):
    query = 'SELECT processes.*, parties_involved.name, roles.name '\
            'FROM processes '\
            'INNER JOIN parties_involved as pi ON processes.id = pi.process_id '\
            'INNER JOIN roles ON roles.id = pi.role_id;'\
            'WHERE processes.number = {};'.format(process_number)
    return __execute_query__(conn, query)

def insert_process(conn, process_args, parties_arg):
    try:
        query_process = 'INSERT INTO processes VALUES ({}) RETURNING * ;'.fomart(args)
        [inserted_process] = conn.cursor().execute(query_process)
        query_parties = 'INSERT INTO parties_involved VALUES ({}) RETURNING * ;'.fomart(args)
        [inserted_parties] = conn.cursor().execute(query_parties)
        conn.commit()

        return inserted_process, inserted_parties
    except Exception as error:
        print(error)

def update_process_movements(conn, process_number, changes):
    query = 'UPDATE processes SET changes = {}'\
            'WHERE processes.number = {} '\
            'RETURNING * ;'.format(changes, process_number)

    [updated_record] = __execute_query__(conn, query)
    conn.commit()
    return updated_record
