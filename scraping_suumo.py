import math
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)

base_url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=020&bs=040&ta=04&sa=01&sngz=&po1=25&po2=99&pc=100&page=2'


def house_url_scraping(url):
    driver.get(url)
    detail_url_list = []

    # ページの量を調べる
    house_amount_element = driver.find_elements(by=By.XPATH, value='//*[@id="js-leftColumnForm"]/div[3]/div[2]/div')[
        0].text
    house_amount = house_amount_element.replace(',', '').replace('件', '')
    print(int(house_amount))
    max_page = math.floor(int(house_amount) / 100 - 1)
    print(max_page)

    # range(max_page)を代入する
    for page in range(2, max_page):
        print(page)
        for house in driver.find_elements(by=By.XPATH, value='//div/h2/a'):
            detail_url = house.get_attribute('href')
            detail_url_list.append(detail_url)

        next_page = driver.find_element(by=By.XPATH, value='//*[@id="js-leftColumnForm"]/div[11]/div[2]/p[2]/a')
        driver.get(next_page.get_attribute('href'))
    return detail_url_list


def detail_elm_scraping(url):
    # 物件詳細urlを読み込み各要素を取り出す。
    try:
        driver.get(url)
        # 家賃など
        fee_list = driver.find_element(By.CLASS_NAME, "property_view_main").text.splitlines()
        rent = fee_list[0].rstrip("万円 ")
        administrative_expenses = fee_list[1].lstrip("管理費・共益費 ").rstrip("円")

        # 間取りなど
        building_list = driver.find_element_by_css_selector(
            ".property_view_detail.property_view_detail--floor_type").text.splitlines()
        plan = building_list[1].lstrip("間取り ")
        area = building_list[2].lstrip("専有面積 ").rstrip("m2")
        building_type = building_list[4].lstrip("建物種別 ")
        building_age = building_list[5].lstrip("築年数 ")

        # アクセス
        access_list = driver.find_element_by_css_selector(".property_view_detail.property_view_detail--train")
        access = access_list.text.replace('\n', '').lstrip("アクセス")

        # 所在地
        location_list = driver.find_element_by_css_selector(".property_view_detail.property_view_detail--location")
        location = location_list.text.splitlines()[1]  # [0]='所在地'

        # 部屋の特徴・設備
        features = driver.find_element_by_css_selector(".bgc-wht.ol-g").text

        # 物件概要
        overview = driver.find_element_by_css_selector(".data_table.table_gaiyou").text
        inp_list = [
            rent,
            administrative_expenses,
            plan,
            area,
            building_type,
            building_age,
            access,
            location,
            features,
            overview
        ]
        return inp_list
    except selenium.common.exceptions.NoSuchElementException:
        print("要素が見つかりませんでした")
    except selenium.common.exceptions.WebDriverException:
        print("ドライバーが見つかりませんでした")
