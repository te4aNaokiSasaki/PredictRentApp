import pandas as pd
import re

data = pd.read_csv("./detail_data.csv", index_col=0)
data = data.dropna(how='all')

l = list["家賃・管理費", "間取り.", "面積.", "種別.", "築年数", "アクセス", '区', "所在地", "バス・ユニットバス", "駐車場", "角部屋", "ロフト", "2人居住", "ペット可",
         "セキュリティ会社", "在宅BOX", "独立洗面台", "階"]

# 家賃・管理費
fee_list = data['家賃'] * 10000 + data['管理費'].replace('-', 0).astype('float64')
fee = pd.Series(fee_list)

# 間取り、面積、種別
plan = data['間取り']
area = data['面積']
house_type = data['種別']

# 築年数
year = pd.Series(data['築年数'].str.rstrip('年'))

# アクセス
'''
access_list = []
for x in data['アクセス']:
    start = x.find('歩')
    end = x.find('分')
    target = x[start + 1:end]
    if target == "":
        access_list.append('99')
    else:
        access_list.append(x[start + 1:end])
access = pd.Series(access_list).astype('float64')
'''
# 所在地
a = data['所在地'].str.replace('宮城県仙台市', '').str.split('区', expand=True)
location_big = pd.Series(a[0])
location_detail = pd.Series(a[1])

# 和室
tatami = pd.Series(data['特徴'].str.count('和室')).replace(0, False).astype(bool)

# ユニットバス
not_unit_bus = pd.Series(data['特徴'].str.count('バストイレ別')).replace(0, False).astype(bool)

# 独立洗面台
free_vanity = pd.Series(data['特徴'].str.count('洗面所独立')).replace(0, False).astype(bool)

# 駐車場
have_parking = pd.Series(data['特徴'].str.count('駐車場')).replace(0, False).astype(bool)

# 角部屋
corner_room = pd.Series(data['特徴'].str.count('角部屋')).replace(0, False).astype(bool)

# ロフト
loft = pd.Series(data['特徴'].str.count('ロフト')).replace(0, False).astype(bool)

# 2人住居
two_people = pd.Series(data['特徴'].str.count('二人入居')).replace(0, False).astype(bool)

# ペット可
pets_allowed = pd.Series(data['特徴'].str.count('ペット')).replace(0, False).astype(bool)
# 宅配BOX
delivery_BOX = pd.Series(data['特徴'].str.count('宅配BOX')).replace(0, False).astype(bool)

# セキュリティ会社
join_security = pd.Series(data['特徴'].str.count('セキュリティ会社')).replace(0, False).astype(bool)
'''
# 階数
floor_list = []
for x in data['その他']:
    start = x.find('階/')
    end = x.find('')
    target = x[start - 1:start]
    if target.isnumeric():
        floor_list.append(target)
    else:
        floor_list.append(1)
floor = pd.Series(floor_list)

# 構造
structure_list = []
for x in data['その他']:
    start = x.find('構造')
    end = x.find('\n')
    structure_list.append(x[start + 3:end])
structure = pd.Series(structure_list)
'''
input_df = pd.DataFrame(
    {'家賃': fee, '間取り': plan, '面積': area, '種別': house_type, "築年数": year, "所在地（区）": location_big,
     "所在地（町）": location_detail, "和室": tatami, "ユニットバス": not_unit_bus, "独立洗面台": free_vanity, "駐車場": have_parking,
     "角部屋": corner_room, "ロフト": loft, "2人居住": two_people, "ペット可": pets_allowed, "宅配BOX": delivery_BOX,
     "セキュリティ会社": join_security}).dropna()

input_df.to_csv('machine_learning/input/input.csv')
