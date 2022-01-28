import pandas as pd
import scraping_suumo

base_url = 'https://suumo.jp/jj/chintai/ichiran/FR301FC005/?ar=020&bs=040&ta=04&sa=01&sngz=&po1=25&po2=99&pc=100&page=2'
data = pd.Series(data=scraping_suumo.house_url_scraping(base_url), name='url')
data.to_csv('detail_url_data.csv', index=False)

