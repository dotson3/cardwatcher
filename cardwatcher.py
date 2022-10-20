import smtplib
import random
import sys

import requests
from bs4 import BeautifulSoup


def get_page_html(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
    page = requests.get(url, headers=headers)
    print(page.status_code)
    return page.content


def check_item_in_stock(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    out_of_stock_divs = soup.findAll('div', {"class": "c-button c-button-disabled c-button-lg c-button-block add-to-cart-button"})  # <--- change "text" to div
    print(out_of_stock_divs)
    return len(out_of_stock_divs) != 0



def check_inventory():
    url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440"
    page_html = get_page_html(url)
    if check_item_in_stock(page_html):
        print("In stock")

        gmail_user = 'geforce308010gb@gmail.com'
        gmail_password = '0p9ol8ik!'

        sent_from = gmail_user
        to = ['ddotson321@gmail.com']
        subject = '3080 10gig in stock!'
        body = ' buy it now!! $699.99  - ' \
               'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'

        email_text = """\
                                               From: %s
                                               To: %s
                                               Subject: %s

                                               %s
                                               """ % (sent_from, ", ".join(to), subject, body)

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print("Email sent successfully!")
            sys.exit()
        except Exception as ex:
            print("Something went wrong….", ex)


    else:
        print('Out of stock -nvidia-geforce-rtx-3080 -10gb')

from time import time, sleep
while True:

    random_wait_time = random.randrange(60,1800)
    print('next search',random_wait_time ,'seconds, checking 3080 10gig stock..')
    sleep(random_wait_time - time() % random_wait_time)

    check_inventory()