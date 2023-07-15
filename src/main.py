import os
from pprint import pprint

from src.config import config
from src.utils import get_hhRU_data, create_database, save_data_to_database
from src.connecting_database import DBManager





def main():

    company_ids = ['4117901', '1740', '8582', '242319', '1942330', '1582752',
                   '4657939', '60377', '9163125', '176941'
                   ]
    params = config()

    data = get_hhRU_data(company_ids)
    create_database('coursework_hh_ru', params)
    save_data_to_database(data, 'coursework_hh_ru', params)
    information = DBManager()
    information.get_companies_and_vacancies_count()


if __name__ == '__main__':
    main()