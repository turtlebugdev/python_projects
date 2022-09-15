import requests

from bs4 import BeautifulSoup
from email.message import EmailMessage
from multiprocessing import context
# from cl_scrape import title_elem
# from cl_scrape import url_elem
# from cl_scrape import price_elem

import ssl
import smtplib
email_sender = 'turtlebugdevpythonemail@gmail.com'
email_password = 'shlsovoqhkweiqwg'

email_receiver = 'robert.j.broughton@gmail.com'

subject = 'Car List'
 
# URL = "https://charlotte.craigslist.org/search/cta?query=Toyota+Prius"
# URL = "https://charlotte.craigslist.org/search/sss"
# URL = "https://charlotte.craigslist.org/search/sss?query=trapezoid+vault"
# URL = "https://charlotte.craigslist.org/search/sss?query=dungeons+dragons"

URL = "https://toledo.craigslist.org/search/cta?purveyor=owner&query=toyota%20prius"
page = requests.get(URL)
soup = BeautifulSoup(page.content,"html.parser")
results = soup.find(class_ ="rows")
car_elems = results.find_all('li',class_="result-row")

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






body = print(carlist)


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())


# shlsovoqhkweiqwg