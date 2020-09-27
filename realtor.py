from bs4 import BeautifulSoup
import requests
import xlsxwriter

number = 1
counter = 0
row = 0
wb = xlsxwriter.Workbook('try002.xlsx')
sheet = wb.add_worksheet()
while number <= 720:
    url = 'https://www.realtor.com/realestateandhomes-search/New-York_NY/pg-{}'.format(number)
    base = 'https://www.realtor.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    container = soup.find_all('li', class_='js-quick-view')
    # print(container)
    for con in container:
        link = base + con['data-url']
        try:
            price = con.find('span', class_='data-price').text
        except:
            price = 'no price found'
        try:
            status = con.find('div', class_='property-type').text
        except:
            status = 'no type found'
        try:
            bed = con.find('li', {'data-label': 'property-meta-beds'}).text
        except:
            bed = 'no bed found'
        try:
            bath = con.find('li', {'data-label': 'property-meta-baths'}).text
        except:
            bath = 'no bath found'
        try:
            area = con.find('li', {'data-label': 'property-meta-sqft'}).text
        except:
            area = 'no area found'
        try:
            area2 = con.find('li', {'data-label': 'property-meta-lotsize'}).text
        except:
            area2 = 'no area found'
        try:
            garage = con.find('li', {'data-label': 'property-meta-garage'}).text
        except:
            garage = 'no garage found'
        try:
            address = con.find('div', {'data-label': 'property-address'}).a.text.strip()
            address = ' '.join(address.split())
        except:
            address = 'no address found'
        sheet.write(row, 0, address)
        sheet.write(row, 1, price)
        sheet.write(row, 2, status)
        sheet.write(row, 3, bed)
        sheet.write(row, 4, bath)
        sheet.write(row, 5, area)
        sheet.write(row, 6, area2)
        sheet.write(row, 7, garage)
        sheet.write(row, 8, link)
        counter += 1
        row += 1
        print(counter)
    number += 1
    print(url)
wb.close()
