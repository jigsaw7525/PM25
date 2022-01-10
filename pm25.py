import pandas as pd


def get_pm25(type=0):
    url = "https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=csv"
    df = pd.read_csv(url).dropna()
    columns = ["county", "Site", "PM25"]
    values = df[columns].values.tolist()
    if type == 1:
        values = sorted(values, key=lambda x: x[-1], reverse=True)
    elif type == 2:
        values = sorted(values, key=lambda x: x[-1], reverse=False)
    return columns, values
