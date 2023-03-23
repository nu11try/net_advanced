import json
import unicodedata

import requests
from bs4 import BeautifulSoup

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/111.0.0.0 Safari/537.36'
}
url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

key_words = ['django', 'flask']


def parser():
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    vacancies = soup.find_all('a', class_='serp-item__title')

    result = []

    for vacancy in vacancies:
        buf_url = vacancy['href']

        response = requests.get(url=buf_url, headers=headers)

        bs = BeautifulSoup(response.text, 'lxml')

        description = bs.find('div', {'data-qa': 'vacancy-description'})

        if key_words[0] in description.text.lower() and key_words[1] in description.text.lower():
            title = bs.find('div', class_='vacancy-title')

            if title:
                salary = unicodedata.normalize('NFKD', title.find('span',
                                                                  class_='bloko-header-section-2 '
                                                                         'bloko-header-section-2_lite').text)
                company = bs.find('a', class_='bloko-link bloko-link_kind-tertiary').find('span').text

                city = bs.find('div', class_='vacancy-company-redesigned').find('p')
                if city:
                    city = city.text
                else:
                    city = bs.find('a', class_='bloko-link bloko-link_kind-tertiary bloko-link_disable-visited').find(
                        'span').text.split(',')[0]

                result.append({
                    'Ссылка на вакансию': buf_url,
                    'Зарплата': salary,
                    'Компания': company,
                    'Город': city,
                })
    return result


if __name__ == '__main__':
    url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

    result_vacancies = parser()

    with open('hh_vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(result_vacancies, file, indent=2, ensure_ascii=False)
