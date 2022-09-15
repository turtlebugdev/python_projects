import requests

from bs4 import BeautifulSoup

URL = "https://toledo.craigslist.org/search/cta?purveyor=owner&query=toyota%20prius"
# URL = "https://charlotte.craigslist.org/search/cta?query=Toyota+Prius"
# URL = "https://charlotte.craigslist.org/search/sss"
# URL = "https://charlotte.craigslist.org/search/sss?query=trapezoid+vault"
# URL = "https://charlotte.craigslist.org/search/sss?query=dungeons+dragons"

page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(class_ ="rows")
car_elems = results.find_all('li',class_="result-row")
print('start')
carlist = []
for car_elem in car_elems:
    price_elem = car_elem.find('span', class_='result-price')
    url_elem = car_elem.find('a', class_ ="result-image")
    title_elem = car_elem.find('a', class_="result-title hdrlnk")
    list = [title_elem.text.strip(),price_elem.text.strip(),url_elem['href']]
    carlist.append(list)
    # print(title_elem.text.strip())
    # print(url_elem['href'])
    # print(price_elem.text.strip())
    # print()


# for car_elem in car_elems:
#     print(price_elem.text)
print(carlist)
print('stop')