--получение списка всех компаний и количество вакансий у каждой компании
SELECT title_company, number_vacancies FROM company

--получение списка всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
SELECT  title_company, vacancy_name, salary_from, salary_to, alternate_url
FROM company_vacancies
INNER JOIN company USING (company_id)

--получение средней зарплаты по вакансиям
SELECT title_company, ROUND(AVG(salary_from))
FROM company_vacancies
INNER JOIN company USING (company_id)
WHERE salary_from > 0
GROUP BY title_company

--получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям
SELECT vacancy_name
FROM company_vacancies
WHERE salary_from > (SELECT AVG(salary_from) FROM company_vacancies)

--получение списка всех вакансий, в названии которых содержатся переданные в метод слова, например “python”
SELECT vacancy_name
FROM company_vacancies
WHERE vacancy_name LIKE '%СЛОВОВ%'
--заменить СЛОВО на интересующее слово
