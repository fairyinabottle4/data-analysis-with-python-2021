#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    a = df["Päivämäärä"]
    b = a.str.split(expand=True)
    b.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    weekdays = {
        'ma': 'Mon',
        'ti': 'Tue',
        'ke': 'Wed',
        'to': 'Thu',
        'pe': 'Fri',
        'la': 'Sat',
        'su': 'Sun'
    }
    months = {
        'tammi': 1,
        'helmi': 2,
        'maalis': 3,
        'huhti': 4,
        'touko': 5,
        'kesä': 6,
        'heinä': 7,
        'elo': 8,
        'syys': 9,
        'loka': 10,
        'marras': 11,
        'joulu': 12
    }
    c = b['Weekday']
    d = c.map(weekdays)
    b['Weekday'] = d
    e = b['Month']
    f = e.map(months)
    f = f.map(int)
    b['Month'] = f
    g = b['Hour']
    h = g.map(lambda x: x[:2])
    h = h.map(int)
    b['Hour'] = h
    i = b['Day']
    i = i.map(int)
    b['Day'] = i
    j = b['Year']
    j = j.map(int)
    b['Year'] = j
    return (b, df)

def split_date_continues():
    dates, df = split_date()
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    df.drop(["Päivämäärä"], axis=1, inplace=True)
    final = pd.concat([dates, df], axis=1)
    return final

def cycling_weather_continues(station):
    weather_df = pd.read_csv('src/kumpula-weather-2017.csv')
    df = split_date_continues()

    new_df = pd.merge(df.loc[:, 'Weekday':'Hour'], df.loc[:, station], left_index=True, right_index=True)
    new_df = new_df[new_df.Year == 2017]
    a = new_df.groupby(['Month', 'Day'])[station].sum()
    merged_df = pd.merge(weather_df, a, right_on=['Day', 'Month'], left_on=['d', 'm'])
    merged_df.fillna(method='ffill', inplace=True)
    model = LinearRegression(fit_intercept=True)
    x = merged_df.loc[:, ['Precipitation amount (mm)', 'Snow depth (cm)', 'Air temperature (degC)']]
    y = merged_df.loc[:, station]
    model.fit(x, y)
    score = model.score(x, y)
    return model.coef_, score
    
def main():
    coef, score = cycling_weather_continues("Baana")
    print(f"Measuring station: Baana")
    print(f"Regression coefficient for variable 'precipitation': {coef[0]:.1f}")
    print(f"Regression coefficient for variable 'snow depth': {coef[1]:.1f}")
    print(f"Regression coefficient for variable 'temperature': {coef[2]:.1f}")
    print(f"Score: {score:.2f}")


if __name__ == "__main__":
    main()
