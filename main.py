import requests
from bs4 import BeautifulSoup
import pprint
import os

import smtplib

GMAIL_SMTP = "smtp.gmail.com"
TEST_EMAIL = os.getenv('TEST_EMAIL')
PASS = os.getenv('PASSWORD')

URL = 'https://www.amazon.in/Lectro-Hero-Electric-Unisex-Frame-46/dp/B099N97FZ9/ref=sr_1_6?crid=2FL7BD6KDC8Y9&keywords=electric+cycle&qid=1652154284&refinements=p_72%3A1318476031&rnid=1318475031&sprefix=electric+c%2Caps%2C356&sr=8-6'
headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

responce = requests.get(headers=headers, url=URL)
page_code = responce.text

soup = BeautifulSoup(page_code, 'lxml')

price = soup.find('span', class_="a-price-whole").get_text().replace(',', '').replace('.', '')
price = int(price)


if price < 31200:
    server = smtplib.SMTP(GMAIL_SMTP)
    server.starttls()
    server.login(user=TEST_EMAIL, password=PASS)

    server.sendmail(
        from_addr=TEST_EMAIL,
        to_addrs='alexasha992@gmail.com',
        msg=f"Price go down, price now is {price}"
    )
    server.close()