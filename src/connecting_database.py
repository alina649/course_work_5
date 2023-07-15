from typing import List, Tuple, Any

import psycopg2


class DBManager:
    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        conn = psycopg2.connect(host='localhost', database='coursework_hh_ru', user='postgres', password='123406@aLINA',
                                port=5432)  # Данные БД
        cur = conn.cursor()  # Включение курсора
        cur.execute("""SELECT title_company, number_vacancies FROM company""")
        rows = cur.fetchall()
        for i in rows:
            name_company = i[0]
            count_vacancy = i[1]
            print(f'{name_company}: Количество вакансий - {count_vacancy}')
        cur.close()  # Закрываем курсор
        conn.close()  # Закрываем


