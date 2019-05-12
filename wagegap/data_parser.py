from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import datetime
import calendar

def parse_min_wages():
    COUNTRIES = ['Belgium', 'Bulgaria', 'Czech Republic', 'Estonia',
     'Poland', 'Germany', 'France', 'United Kingdom',
     'Greece', 'Hungary', 'Ireland', 'Latvia', 'Lithuania',
     'Luxembourg', 'Netherlands', 'Romania', 'Portugal', 'Slovakia',
     'Slovenia', 'Spain', 'Switzerland']

    MONTHS = dict((v,k) for k, v in enumerate(calendar.month_name))

    URL_DATA = 'https://en.wikipedia.org/wiki/List_of_European_countries_by_minimum_wage'
    context = ssl._create_unverified_context()
    serialized_data = urlopen(URL_DATA, context=context)

    min_wages = []

    soup = BeautifulSoup(serialized_data, features="html.parser")

    table = soup.find('table', attrs={'class': 'wikitable sortable'})
    table_body = table.find('tbody')

    for row in table_body.find_all('tr'):
        for el in row.find_all('td'):
            for x in el.find_all('a'):
                if x.string in COUNTRIES:
                    country = x.string
                    y = row.find_next('td', attrs={'style': 'background:#bfe4ff;'})
                    wage = int(list(y.children)[0].string.split()[0])
                    date = list(row.children)[-1].string.split()
                    date = datetime.date(int(date[-1]), MONTHS[date[-2]], int(date[-3]))
                    min_wages.append((country, wage, date))

    return min_wages

def parse_price2spending_dict(country_name):
    URL_DATA = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country='+country_name+'&displayCurrency=EUR'
    context = ssl._create_unverified_context()
    serialized_data = urlopen(URL_DATA, context=context)

    soup = BeautifulSoup(serialized_data, features="html.parser")
    data = soup.get_text().replace('\xa0', ' ').split("\n")

    price2spending = {}
    for item in data:
        if chr(8364) in item:
            item = item.strip().split("  ")
            price2spending[item[0]] = float(item[-1][:-2].strip().replace(',', ''))

    del price2spending['Average Monthly Net Salary (After Tax)']
    return price2spending

def parse_spending2category_dict():
    URL_DATA = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=Poland&displayCurrency=EUR'
    context = ssl._create_unverified_context()
    serialized_data = urlopen(URL_DATA, context=context)

    soup = BeautifulSoup(serialized_data, features="html.parser")
    data = soup.get_text().replace('\xa0', ' ').split("\n")

    spending2category = {}

    category='No category'
    for item in data:
        if '[ Edit ]' in item:
            category = item.strip('[ Edit ]')
            spending2category[category] = []
        if chr(8364) in item:
            item = item.strip().split("  ")
            spending2category[category].append(item[0])
    del spending2category['Salaries And Financing']

    return spending2category

def main():
    print(parse_min_wages())
    print(parse_spending2category_dict())
    print(parse_price2spending_dict('France'))


if __name__ == '__main__':
    main()
