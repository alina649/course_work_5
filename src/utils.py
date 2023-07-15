from pprint import pprint
from typing import Any
import psycopg2
import requests

from src.config import config


def get_hhRU_data(company_ids: list[str]):
    """Получение данных с сайта HH_ru"""
    data = []
    for company_id in company_ids:
        url_company = f'https://irkutsk.hh.ru/employers/{company_id}'

        url_vacancy = 'https://api.hh.ru/vacancies'
        params = {'employer_id': company_id,
                  'per_page': '10'}
        headers = {
            "User-Agent": "50355527",  # Replace with your User-Agent header
        }
        response_vacancy = requests.get(url_vacancy, params=params, headers=headers)
        response_company = requests.get(url_company, headers=headers)

        if response_vacancy.status_code == 200:
            dat_v = response_vacancy.json()
            dat_c = response_company.json()
            data.append({'company': dat_c,'vacancy': dat_v['items']})
    return data


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных о каналах и видео."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")  # Удаление базы данных
    cur.execute(f"CREATE DATABASE {database_name}")  # создание БД

    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE company (
                company_id SERIAL PRIMARY KEY,
                title_company VARCHAR(255),
                number_vacancies INTEGER
            );
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE company_vacancies (
                vacancy_name TEXT,
                company_id INT REFERENCES company(company_id),
                salary_from INTEGER,
                salary_to INTEGER,
                alternate_url TEXT
            );
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict):
    """Сохранение данных о каналах и видео в базу данных."""

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:

        for companys in data:
            number_vacancies = companys['found']
            for company in companys['items']:
                company_id = company['employer']['id']
                title_company = company['employer']['name']

                cur.execute(
                    """
                    INSERT INTO  company (company_id, title_company, number_vacancies)
                    VALUES (%s, %s, %s)
                    """,
                    (company_id, title_company, number_vacancies)
                )

                vacancy_name = company['name']
                if company['salary'] is not None:
                    salary_from = company['salary']['from']
                    salary_to = company['salary']['to']
                else:
                    salary_from = 0
                    salary_to = 0
                alternate_url = company['alternate_url']
                cur.execute(
                    """
                        INSERT INTO company_vacancies (company_id, vacancy_name, salary_from, salary_to, alternate_url)
                        VALUES (%s, %s, %s, %s, %s)
                        """,
                    (company_id, vacancy_name, salary_from, salary_to, alternate_url)
                )

    conn.commit()
    conn.close()
