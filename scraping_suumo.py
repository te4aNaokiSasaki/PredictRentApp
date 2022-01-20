import csv
import math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("C:\\Users\\naoki\\Downloads\\chromedriver", options=options)

base_url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=020&bs=040&ta=04&sa=01&sngz=&po1=25&po2=99&pc=100&page=2'


def house_url_scraping(url):
    driver.get(url)
    detail_url_list = []

    # ページの量を調べる
    house_amount_element = driver.find_elements(by=By.XPATH, value='//*[@id="js-leftColumnForm"]/div[3]/div[2]/div')[0].text
    house_amount = house_amount_element.replace(',', '').replace('件', '')
    print(int(house_amount))
    max_page = math.floor(int(house_amount) / 100 - 1)
    print(max_page)

    # range(max_page)を代入する
    for page in range(max_page):
        print(page)
        for house in driver.find_elements(by=By.XPATH, value='//div/h2/a'):
            detail_url = house.get_attribute('href')
            detail_url_list.append(detail_url)

        next_page = driver.find_element(by=By.XPATH, value='//*[@id="js-leftColumnForm"]/div[11]/div[2]/p[2]/a')
        driver.get(next_page.get_attribute('href'))
    return detail_url_list


def search_next_page_url(url):
    next_page_url = driver.find_element(by=By.XPATH, value='//*[@id="js-leftColumnForm"]/div[11]/div[2]/p[2]/a')
    driver.get(next_page_url.get_attribute('href'))
    return next_page_url


def detail_scraping(url):
    driver.get(url)
    detail_elm_list = []

    try:
        x = driver.find_elements(by=By.XPATH, value='//*[@id="contents"]/div[4]/table')
        print(x[0])
    except IndexError:
        print("例外発生")


def with_video(url):
    is_with_video = False

    return is_with_video


def save_data(list, file):
    f = open(file, mode="w", newline="")
    writer = csv.writer(f)
