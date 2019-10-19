import psycopg2 as pg
import credentials

class Database:
    def __init__(self):
        self.params = credentials.build()
        self.conn = None
        self.cursor = None

    def __execute_query__(self, query):
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except (Exception, pg.DatabaseError) as error:
            print(error)


    def open(self):
        try:
            self.conn = pq.connect(**self.params)
            self.cursor = self.conn.cursor()

        except error:
            print(error)
        finally:
            if self.conn is not None:
                self.conn.close()

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.cursor.close()

    def get_courts(self, process_number, court):
        query = 'SELECT * FROM courts;'
        return __execute_query__(query)

    def get_process(self, process_number, court):
        query = 'SELECT processes.*, parties_involved.name, roles.name '\
                'FROM processes '\
                'INNER JOIN parties_involved as pi ON processes.id = pi.process_id '\
                'INNER JOIN roles ON roles.id = pi.role_id;'\
                'WHERE processes.number = {} AND court_id = {}'
                .format(process_number, court)
        return __execute_query__(query)

    def update_process_movements(self, process_number, court, changes):
        query = 'UPDATE processes SET changes = {}'\
                'WHERE processes.number = {} AND court_id = {}'
                .format(changes, process_number, court)

        return __execute_query__(query)
