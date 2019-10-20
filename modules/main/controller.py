from datetime import datetime, timedelta
import modules.db.database as db
from modules.main import crawler, formatter


def __make_request(process_number):
    crawler = CourtCrawler()

    status, html_text = crawler.get_process(process_number)
    html_parsed = fomatter.parseHTML(html_text)

    process_info = formatter.find_process_info(html_parsed)
    parties_involved = formatter.find_parties_involved(html_parsed)
    changes = formatter.find_changes(html_parsed)
    print(process_info)
    print(parties_involved)
    print(changes)
    print("E agora, como insere? heheheh")
    # result = insert_process({process_info, changes}, parties_involved)
    return

def __last_access_less_than_a_day(date):
    DAY_IN_SECONDS = 24*60*60
    delta = datetime.now() - date
    return delta.seconds < DAY_IN_SECONDS

def get_courts():
    conn = db.open()
    results = db.get_courts(conn)
    db.close(conn)
    return results

def get_process_info(process_number):
    conn = db.open()
    result = db.get_process(conn, process_number)

    if(result == []):
        result = db.insert_process(conn, process_args, parties_arg)

    if(__last_access_less_than_a_day(result.last_access)):
        db.close(conn)
        print(result)
        return result
    else:
        coisas_novas = __make_request(process_number)
        print(coisas_novas)
        # se tiver algo diferente, atualiza a base de dados
        result = db.update_process_movements(conn, process_number, changes)

    db.close(conn)
    print(result)
    return result
