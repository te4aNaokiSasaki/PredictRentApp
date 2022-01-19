from selenium import webdriver
from time import sleep
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome("C:\\Users\\naoki\\Downloads\\chromedriver",options=options)
base_url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=020&bs=040&ta=04&sa=01&sngz=&po1=25&po2=99&pc=100'


def base_scripting(url):
    driver.get(url)
    detail_url_list = []
    for element in driver.find_elements(by=By.XPATH, value='//div/h2/a'):
        detail_url = element.get_attribute('href')
        detail_url_list.append(detail_url)
    return detail_url_list

def detail_scripting(url_list):
    for url in url_list:
        driver.get(url)
        yatin = driver.find_elements(by=By.XPATH, value='//div/div[1]')
        print(yatin)
