import csv
import math

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)

dict = {"家賃": "",
        "管理費・共益費": "",
        "所在地": "",
        "駅徒歩": "",
        "間取り": "",
        "占有面積": "",
        "築年数": "",
        "階": "",
        "建物種別": "",
        "特徴・設備": "",
        "間取り詳細": "",
        "構造": "",
        "階詳細": "",
        "駐車場": "",
        "条件": ""
        }

with open('detail_url_data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        for i in range(10):
            driver.get(row[i])
            print(row[i])
            # 家賃など
            tableElem0 = driver.find_element(By.CLASS_NAME, "property_view_main")
            # print(tableElem0.text)
            list0 = tableElem0.text.splitlines()
            print(list0)
            # 所在地・間取りなど
            tableElem1 = driver.find_element(By.CLASS_NAME, "l-property_view_detail")
            # print(tableElem1.text)
            list1 = tableElem1.text.splitlines()
            print(list1)
            # 部屋の特徴・設備
            tableElem2 = driver.find_element_by_css_selector(".bgc-wht.ol-g")
            print(tableElem2.text)
            # 物件概要
            tableElem3 = driver.find_element_by_css_selector(".data_table.table_gaiyou")
            # print(tableElem3.text)
            list3 = tableElem3.text.splitlines()
            print(list3)



