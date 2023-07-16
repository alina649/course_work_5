# course_work_5

## Файл utils.py

-Получены данные о работадателях с сайта [hh.ru](https://api.hh.ru/employers/).

-Получены данные о вакансиях с сайта  [hh.ru](https://api.hh.ru/vacancies).

-Код создает и заполняет таблицы в БД Postgres данными о работодателях и их вакансиях.

- Выбрать не менее 10 интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
- 
- Спроектировать таблицы в БД Postgres для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используйте библиотеку `psycopg2`.
- 
- Реализовать код, который заполняет созданные таблицы в БД Postgres данными о работодателях и их вакансиях.
- 
- Создать класс `DBManager` для работы с данными в БД.

## Файл connecting_database.py

-Реализован класс `DBManager` для работы с данными в БД.

-Класс `DBManager` должен использовать библиотеку `psycopg2` для работы с БД.

-Методы Класса 'DBManager'
- `get_companies_and_vacancies_count()`: получает список всех компаний и количество вакансий у каждой компании.
- `get_all_vacancies()`: получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
- `get_avg_salary()`: получает среднюю зарплату по вакансиям.
- `get_vacancies_with_higher_salary()`: получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
- `get_vacancies_with_keyword()`: получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.

## Файл main.py
-активирует код с файлов connecting_database.py и connecting_database.py.

-реализует контакт с пользователем.


