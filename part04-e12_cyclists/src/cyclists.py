#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv('src/Helsingin_pyorailijamaarat.csv', sep=';')
    df.dropna(how='all', inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    print(df)
    print(df.shape)
    return df


def main():
    cyclists()
    
if __name__ == "__main__":
    main()
