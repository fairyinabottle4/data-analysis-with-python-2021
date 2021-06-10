#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv('src/who_suicide_statistics.csv', sep=',', index_col="country")
    df.drop(["year", "sex", "age"], axis=1, inplace=True)
    df["mean"] = df["suicides_no"] / df["population"]
    df2 = df.groupby("country")
    df3 = df2["mean"].mean()
    # print(df3)
    return df3
    
def suicide_weather():
    suicide = suicide_fractions()
    weather = pd.read_html('src/List_of_countries_by_average_yearly_temperature.html', index_col="Country")[0]
    weather = weather.iloc[:, 0].str.replace("\u2212", "-").astype(float)
    new_df = pd.merge(weather, suicide, left_index=True, right_index=True)
    correlation = new_df.corr(method='spearman').iloc[0, 1]
    (suicide_rows, temperature_rows, common_rows) = (x.shape[0] for x in [suicide, weather, new_df])
    return suicide_rows, temperature_rows, common_rows, correlation

def main():
    suicide_rows, temperature_rows, common_rows, correlation = suicide_weather()
    print(f"Suicide DataFrame has {suicide_rows} rows")
    print(f"Temperature DataFrame has {temperature_rows} rows")
    print(f"Common DataFrame has {common_rows} rows")
    print(f"Spearman correlation: {correlation}")

if __name__ == "__main__":
    main()
