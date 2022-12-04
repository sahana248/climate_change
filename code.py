# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:54:00 2022

@author: sahana muralidaran (21076516)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
This function takes the file name as the input and returns two tables
1. years as columns (country_table)
2. countries as columns (year_table)
"""
def tablefunc(filename):
    data= pd.read_csv(filename,skiprows=4)
    data=data.dropna(how='all', axis='columns')
    #getting a list of column names that are numbers
    year = [val for val in list(data.columns.values) if val.isdigit()]
    #setting the index as country names
    data= data.set_index([pd.Index(data['Country Name'])])
    country_table= data[year]
    year_table = country_table.transpose()
    return(country_table,year_table)

"""
This function takes a list of any 8 countries and plots the percentage
of agricultural land over the years (with a step of 5 years)
"""
def subplots(country):
    #to get a list of years with a step of 5 years
    year = [val for val in list(country_table1.columns.values) if val.isdigit()]
    year= year[-1::-5]
    year_5= year[::-1]
    #creating new dataframe with data from the selected countries and years
    new_data= country_table1.loc[country][year_5]
    fig, axs = plt.subplots(2, 4, figsize=(28, 13))
    #loop for plotting the subplots
    for ind,name in enumerate(country):
        plt.subplot(2,4,ind+1)
        plt.plot(new_data.loc[name])
        plt.title(name)
        plt.xticks(rotation=45.0)
        plt.xlabel('Years')
        plt.ylabel('% of land')
    plt.savefig("subplot.png")
    plt.show()

list_country= ['Brazil','China','India','Mexico','South Africa','United States','United Kingdom','World']
country_table1,year_val= tablefunc('agri_land.csv')
subplots(list_country)

