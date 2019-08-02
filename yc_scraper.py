import requests 
from bs4 import BeautifulSoup
from csv import DictWriter 

base_url = 'https://www.ycombinator.com/topcompanies/'

def scrape_companies():
    all_companies = []
    res = requests.get(f'{base_url}')
    soup = BeautifulSoup(res.text, 'html.parser')
    companies = soup.find_all('tr')




    for company in companies: 
        all_companies.append({
            'company': company.find('b'),
            'rank': company.find(class_='text-center'),
            'description': company.find('p'),
            'founders': company.find(class_='founders').get_text(),
            'sector': company.find(class_='sectors').get_text(),
            'jobs_created': company.find('td', text='JOBS CREATED'),
            #'batch': company.find(class_='').get_text()
        })
    return all_companies
    print('Scraping was successful!')

def write_companies(companies):
    with open('yc_top100.csv', 'w') as file: 
        headers = ['company', 'rank','description','founders','sector', 'jobs_created']
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for company in companies: 
            csv_writer.writerow(company)

companies = scrape_companies()
write_companies(companies)
    