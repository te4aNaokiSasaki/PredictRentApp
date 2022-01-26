from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options

import scraping_suumo
import csv

base_url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=020&bs=040&ta=04&sa=01&sngz=&po1=25&po2=99&pc=100&page=2'

with open("detail_url_data.csv", mode="w") as f:
    writer = csv.writer(f)
    writer.writerow(scraping_suumo.house_url_scraping(base_url))
    f.close()