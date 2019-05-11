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

    return main_wages

def main():
    parse_min_wages()

if __name__ == '__main__':
    main()
