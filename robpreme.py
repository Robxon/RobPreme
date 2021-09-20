from datetime import datetime
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time


def start_bot():
    """ Initialize the program; define color and keyword of the product"""

    print(r"""
     _______             __        _______
    |       \           |  \       |       \
    | $$$$$$$\  ______  | $$____   | $$$$$$$\  ______    ______   ______ ____    ______
    | $$__| $$ /      \ | $$    \  | $$__/ $$ /      \  /      \ |      \    \  /      \
    | $$    $$|  $$$$$$\| $$$$$$$\ | $$    $$|  $$$$$$\|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\
    | $$$$$$$\| $$  | $$| $$  | $$ | $$$$$$$ | $$   \$$| $$    $$| $$ | $$ | $$| $$    $$
    | $$  | $$| $$__/ $$| $$__/ $$ | $$      | $$      | $$$$$$$$| $$ | $$ | $$| $$$$$$$$
    | $$  | $$ \$$    $$| $$    $$ | $$      | $$       \$$     \| $$ | $$ | $$ \$$     \
     \$$   \$$  \$$$$$$  \$$$$$$$   \$$       \$$        \$$$$$$$ \$$  \$$  \$$  \$$$$$$$
     """)
    # Define color of the product and keyword that will be used to detect its name.
    print("Let's start, define color:")
    color = input()
    print("Define keyword:")
    keyword = input()

    return color, keyword


def initialize_browser():
    """ Opens window with the browser on which the checkout will be performed"""

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.supremenewyork.com/shop/all")
    return driver


def search_for_product(settings, color, keyword):
    """ Searches for product using requests module. Uses search_delay specified in settings."""

    print('Trying to find the product in subpage ', settings['category'])
    did_find_product = False
    while not did_find_product:
        try:
            with requests.Session() as s:

                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) '
                                         'Gecko/20100101 Firefox/80.0'}
                url = settings['category']
                r = s.get(url, headers=headers)

                soup = BeautifulSoup(r.text, 'html.parser')
                my_divs = soup.findAll("div", {"class": "inner-article"})

                for div in my_divs:
                    links = div.findAll("a", {"class": "name-link"})
                    link1 = links[0]
                    link2 = links[1]

                    if keyword in link1.text.lower() or color in link1.text.lower():
                        if keyword in link2.text.lower() or color in link2.text.lower():
                            specific_url = link1.get("href")
                            did_find_product = True
                            product_url = "https://www.supremenewyork.com" + specific_url
                            print('Product:', link1.text, 'detected', 'with URL:', product_url,
                                  'at:', datetime.today().strftime('%H:%M:%S:%f'))
                            return product_url

            print("No match of", keyword, "and ", color, "---> refreshing in", (settings['search_delay']), "seconds ",
                  datetime.today().strftime('%H:%M:%S'))
            time.sleep(float(settings['search_delay']))

        except Exception as e:
            print('An error has occurred:', str(e))
            time.sleep(2)
            print('Retrying:')


def buy_product(product_url, driver, keys):
    """Performing checkout of the product with product_url on previously initialized browser"""

    print('Checkout started', datetime.today().strftime('%H:%M:%S:%f'))
    driver.get(product_url)
    driver.find_element_by_name('commit').click()
    time.sleep(.5)
    checkout_element = driver.find_element_by_class_name('checkout')
    checkout_element.click()

    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(keys['name'])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(keys['email'])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(keys['phone_number'])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(keys['street_address'])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(keys['zip_code'])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(keys['city'])
    driver.find_element_by_xpath('//*[@id="order_billing_country"]').send_keys(keys['country'])
    driver.find_element_by_xpath('//*[@id="vval"]').send_keys(keys['card_cvv'])
    driver.find_element_by_xpath('//*[@id="cnb"]').send_keys(keys['card_number'])
    driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys(keys['card_month'])
    driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys(keys['card_year'])

    # Terms and conditions
    checkboxes = driver.find_elements_by_class_name('iCheck-helper')
    checkboxes[1].click()
    time.sleep(float(keys['checkout_delay']))
    process_payment = driver.find_element_by_class_name('button ')
    process_payment.click()
    print('Checkout finished', datetime.today().strftime('%H:%M:%S:%f'))
