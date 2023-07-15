from typing import List, Tuple, Any

import psycopg2


class DBManager:

    def __init__(self):
        pass

    def get_companies_and_vacancies_count(self):
        conn = psycopg2.connect(host='localhost', database='coursework_hh_ru', user='postgres', password='123406@aLINA',
                                port=5432)  # Данные БД
        cur = conn.cursor()  # Включение курсора
        cur.execute("""SELECT title_company, number_vacancies FROM company""")
        rows = cur.fetchall()
        print(rows)
        for i in rows:
            name_company = i[0]
            count_vacancy = i[1]
            print(f'')
        cur.close()  # Закрываем курсор
        conn.close()  # Закр
