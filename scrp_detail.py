from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome("C:\\Users\\naoki\\Downloads\\chromedriver", options=options)
base_url = 'https://suumo.jp/chintai/bc_100263372077/'
driver.get(base_url)

detail_url_list = []

elm_list = {"家賃": '//*[@id="js-view_gallery"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]',
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
            "構造": '//*[@id="contents"]/div[2]/table/tbody/tr[1]/td[2]',
            "階数": '//*[@id="contents"]/div[2]/table/tbody/tr[2]/td[1]',
            "条件": '//*[@id="contents"]/div[2]/table/tbody/tr[5]/td[1]',
            "駐車場": '//*[@id="contents"]/div[2]/table/tbody/tr[3]/td[2]'
            #"周辺情報": '//*[@id="contents"]/div[2]/table/tbody/tr[13]/td[1]'
            }

for elm in elm_list.values():
    print(driver.find_elements(by=By.XPATH, value=elm)[0].text)
