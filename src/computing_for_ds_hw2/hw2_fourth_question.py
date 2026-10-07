# 10) In a separate file, write a piece of code that
#     loads the covid.csv file and prints the list of countries
#     and the average of the ratio death/confirmed among those countries
#     for those countries that have more than 500, 1000 and 5000
#     active cases respectively.
#     Follow DRY principles in order to complete this exercise.

import pandas as pd
import numpy as np

df = pd.read_csv("covid.csv")

# Exporting csv file contents into numpy lists
# Then printing a list of all the countries in our "covid.csv" file
country = df["Country"].to_numpy()
print(country)

def countries_above_active_cases(n: int):
    """
    Function to create filtered data frame where the number of active cases is greater than or equal to n.
    """
    filtered_df = df[df["Active"] > n]

    ratio = filtered_df["Deaths"]/filtered_df["Confirmed"]

    print(f"\nCountries with greater than {n} active cases:")
    print(filtered_df["Country"].to_list())
    print(f"Average death/confirmed ratio: {ratio.mean()}")

# Loop to display core of code. Note I added -1 because I read it also asking for average ratio of all countries
# "prints the list of countries and the average of the ratio death/confirmed". Implies to calculate ratio for entire data set.
for n in [-1, 500, 1000, 5000]:
    countries_above_active_cases(n)