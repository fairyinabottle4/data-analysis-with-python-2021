#!/usr/bin/env python3

import pandas as pd

def cities():
    indices = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    population = [643272, 279044, 231853, 223027, 201810]
    area = [715.48, 528.03, 689.59, 240.35, 3817.52]
    return pd.DataFrame(data={"Population": population, "Total area": area}, index=indices)

    # df = pd.DataFrame([[643272, 715.48], [279044, 528.03], [231853, 689.59], [223027, 240.35], [201810, 3817.52]], index=indices, columns=["Population", "Total area"])
    # return df

def main():
    print(cities())
    
if __name__ == "__main__":
    main()
