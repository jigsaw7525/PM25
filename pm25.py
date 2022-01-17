import pandas as pd
url = "https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv"
# 從網址抓資料，清除空值
df = pd.read_csv(url).dropna()
# 擷取需要用到的欄位
columns = ["county", "Site", "PM25"]

six_cities = ['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市']

# 預設type=0，不做排列


def get_pm25(type=0):
    # 將dataframe轉換成list
    values = df[columns].values.tolist()

    # 如果type == 1 做升冪排列
    if type == 1:
        values = sorted(values, key=lambda x: x[-1], reverse=True)
    # 如果type == 2 做降冪排列
    elif type == 2:
        values = sorted(values, key=lambda x: x[-1], reverse=False)

    # 將結果return給get_pm25()
    return columns, values


def get_six_pm25():
    six_pm25 = {}
    for city in six_cities:
        six_pm25[city] = round(df.groupby(
            "county").get_group(city)['PM25'].mean(), 1)
    return six_pm25


def get_county():
    countys = []
    for county in df['county']:
        if county not in countys:
            countys.append(county)
    countys = countys[1:]+countys[0:1]
    return countys


def get_county_pm25(county):
    county_pm25 = df.groupby('county').get_group(
        county)[['Site', 'PM25']].values.tolist()
    return county_pm25
