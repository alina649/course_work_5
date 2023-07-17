from src.config import config
from src.utils import get_hhRU_data, create_database, save_data_to_database
from src.connecting_database import DBManager


def main():
    company_ids = ['4117901', '1740', '8582', '242319', '1942330', '1582752',
                   '4657939', '60377', '9163125', '176941'
                   ]
    params = config()

    data = get_hhRU_data(company_ids)  # Получение данных с HH_ru
    create_database('coursework_hh_ru', params)
    save_data_to_database(data, 'coursework_hh_ru', params)

    information = DBManager(params)

    while True:
        human_response = input("Введите цифру того что хотите увидеть:"
                               "\n1-Вывести на экран  список всех компаний "
                               "и количество вакансий у каждой компании?  "
                               "\n2-Вывести на экран список всех вакансий с указанием названия компании,"
                               "названия вакансии и зарплаты и ссылки на вакансию"
                               "\n3-Вывести на экран среднюю зарплату по вакансиям?"
                               "\n4-Вывести на экран список всех вакансий, у которых "
                               "зарплата выше средней по всем вакансиям?"
                               "\n5-Вывести на экран список всех вакансий, в названии "
                               "которых содержатся слова, например “python”?"
                               "\nВведите 'стоп', чтобы выйти"
                               "\nОтвет: ")

        if human_response.lower() == '1':
            information.get_companies_and_vacancies_count()
            continue

        if human_response.lower() == '2':
            information.get_all_vacancies()
            continue

        if human_response.lower() == '3':
            information.get_avg_salary()
            continue

        if human_response.lower() == '4':
            information.get_vacancies_with_higher_salary()
            continue

        if human_response.lower() == '5':
            word = input("Введите слово: ")
            information.get_vacancies_with_keyword(word)
            continue

        if human_response.lower() == 'стоп':
            exit()


if __name__ == '__main__':
    main()
