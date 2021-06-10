#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

def split_date():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    a = df["Päivämäärä"]
    b = a.str.split(expand=True)
    b.columns = ['Weekday', 'Day', 'Month', 'Year', 'Hour']
    weekdays = {
        'ma': 1,
        'ti': 2,
        'ke': 3,
        'to': 4,
        'pe': 5,
        'la': 6,
        'su': 7
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

def bicycle_timeseries():
    a = split_date_continues()
    a["Date"] = pd.to_datetime(a[["Year", "Month", "Day", "Hour"]])
    a.drop(columns=["Year", "Month", "Day", "Hour"], inplace=True)
    a.set_index("Date", inplace=True)
    return a


def commute():
    pd = bicycle_timeseries()
    a = pd["2017-08-01":"2017-08-31"]
    b = a.groupby("Weekday").sum()
    return b
    
def main():
    df = commute()
    df.plot()
    plt.show()


if __name__ == "__main__":
    main()
