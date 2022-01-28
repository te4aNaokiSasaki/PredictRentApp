import pandas as pd
import scraping_suumo

df = pd.DataFrame([], columns=["家賃", "管理費", "間取り", "面積", "種別", "築年数", "アクセス", "所在地", "特徴", "その他"])
url_list = pd.read_csv('detail_url_data.csv')
i = 0
for url in url_list['url']:
    i = i + 1
    if i > 3000:
        break
    df.loc[i] = scraping_suumo.detail_elm_scrp(url)
    print(i)
    print(url)

df.to_csv("detail_data.csv")