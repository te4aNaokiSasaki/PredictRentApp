import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome("C:\\Users\\naoki\\Downloads\\chromedriver", options=options)

base_url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=020&bs=040&ta=04&sa=01&sngz=&po1=25&po2=99&pc=100&page=2'


def house_scraping(url):
    driver.get(url)
    for page in range(1):
        detail_url_list = []
        for house in driver.find_elements(by=By.XPATH, value='//div/h2/a'):
            detail_url = house.get_attribute('href')
            detail_url_list.append(detail_url)

        next_page = driver.find_element(by=By.XPATH, value='//*[@id="js-leftColumnForm"]/div[11]/div[2]/p[2]/a')
        driver.get(next_page.get_attribute('href'))
    return detail_url_list

def detail_scraping(url):
    driver.get(url)
    detail_elm_list = []
    elm_dict = {"名称": '//*[@id="wrapper"]/div[3]/div[1]/h1',
                "家賃": '//*[@id="js-view_gallery"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]',
                "管理費・共益費": '//*[@id="js-view_gallery"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]',
                "敷金": '//*[@id="js-view_gallery"]/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[2]/span[1]',
                "礼金": '//*[@id="js-view_gallery"]/div/div[2]/div[2]/div/div[2]/div/div[2]/ul/li[1]/div/div[2]/span[3]',
                "間取り": '//*[@id="js-view_gallery"]/div/div[2]/div[3]/div[1]/div/div[2]/ul/li[1]/div/div[2]',
                "専有面積": '//*[@id="js-view_gallery"]/div/div[2]/div[3]/div[1]/div/div[2]/ul/li[2]/div/div[2]',
                "建物種別": '//*[@id="js-view_gallery"]/div/div[2]/div[3]/div[1]/div/div[2]/ul/li[4]/div/div[2]',
                "築年数": '//*[@id="js-view_gallery"]/div/div[2]/div[3]/div[1]/div/div[2]/ul/li[5]/div/div[2]',
                "アクセス": '//*[@id="js-view_gallery"]/div/div[2]/div[3]/div[2]/div[1]/div/div[2]',
                "所在地": '//*[@id="js-view_gallery"]/div/div[2]/div[3]/div[2]/div[2]/div/div[2]/div',
                "特徴": '//*[@id="bkdt-option"]/div/ul',
                #動画付き物件だとXPATHが変わる！！
                "構造": '//*[@id="contents"]/div[2]/table/tbody/tr[1]/td[2]',
                "階数": '//*[@id="contents"]/div[2]/table/tbody/tr[2]/td[1]',
                "条件": '//*[@id="contents"]/div[2]/table/tbody/tr[5]/td[1]',
                "駐車場": '//*[@id="contents"]/div[2]/table/tbody/tr[3]/td[2]',
                "周辺情報": '//*[@id="contents"]/div[2]/table/tbody/tr[13]/td[1]'
                }
    for elm in elm_dict.values():
        detail_elm_list.append(driver.find_elements(by=By.XPATH, value=elm)[0].text)
    return detail_elm_list

f = open("data.csv", mode="w", newline="")
writer = csv.writer(f)

list = house_scraping(base_url)
for l in list:
    writer.writerow(detail_scraping(l))
f.close()