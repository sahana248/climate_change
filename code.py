# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:54:00 2022

@author: sahana muralidaran (21076516)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def tablefunc(filename):
    """
    This function takes the file name as the input and returns two tables
    1. years as columns (country_table)
    2. countries as columns (year_table)
    """
    data= pd.read_csv(filename,skiprows=4)
    data=data.dropna(how='all', axis='columns')
    #getting a list of column names that are numbers
    year = [val for val in list(data.columns.values) if val.isdigit()]
    #setting the index as country names
    data= data.set_index([pd.Index(data['Country Name'])])
    country_table= data[year]
    year_table = country_table.transpose()
    print('The table with years as columns:\n', country_table)
    print('The table with country name as columns:\n', year_table)
    return(country_table,year_table)

def multiline_plot(country):
   """
    This function takes a list of G5 countries('Brazil','China','India',
    'Mexico','South Africa' and plots the percentage
    of urban population over the years (with a step of 5 years)
    """
    #to get a list of years with a step of 5 years
    year = [val for val in list(country_table1.columns.values) if val.isdigit()]
    year= year[-1::-5]
    year_5= year[::-1]
    #creating new dataframe with data from the selected countries and years
    new_data= country_table1.loc[country][year_5]
    plt.rcParams["figure.figsize"] = (8,5)
    #loop for plotting the graph
    for ind,name in enumerate(country):
        plt.plot(year_5,new_data.loc[name],label=name)
        plt.legend()
        plt.xticks(rotation=45.0)
        plt.xlabel('Years')
        plt.ylabel('% of urban population')
    plt.title('Change in urban population(1961-2021)')
    plt.savefig("multiline.png")
    plt.show()
def heatmap(country_filename):
    """
    This function takes the file name as input and returns the country's heatmap
    which compares factors like: 
        Urban population, Fertilizer consumption, NO2 emission, 
        methane emmission, agriculture land area
    """
    data= pd.read_csv(country_filename,skiprows=4)
    data=data.dropna(how='all', axis='columns')
    #setting the index as Indicator names
    data= data.set_index([pd.Index(data['Indicator Name'])])
    #creating a list to identify the factors to be used in the heatmap
    ref=['Urban population','Fertilizer consumption (kilograms per hectare of arable land)',
         'Agricultural nitrous oxide emissions (thousand metric tons of CO2 equivalent)',
         'Agricultural methane emissions (thousand metric tons of CO2 equivalent)',
         'Agricultural land (sq. km)']
    heatmap_data=data.loc[ref]
    #creating a set of new label values
    label=['Urban population','Fertilizer consump','NO2 emissions','methane emissions','Agricultural land area']  
    for i,values in enumerate(heatmap_data.index): #for loop to rename index for convenience while plotting the heat map
        heatmap_data=heatmap_data.rename(index={values:label[i]})
    heatmap_data = heatmap_data.drop(['Country Name','Country Code','Indicator Code','Indicator Name'],axis=1)
    final_data=heatmap_data.transpose().corr()
    fig, ax = plt.subplots(figsize=(20,8))
    ax.imshow(final_data)
    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(label)), labels=label)
    ax.set_yticks(np.arange(len(label)), labels=label)
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    for i,value in enumerate(label): #loop to add correlation value to the heatmap
        for j in range(len(label)):
            ax.text(j,i,round(final_data[value][j],3),ha="center", va="center", color="r")       
    ax.set_title("China")
    fig.tight_layout() 
    plt.show()
    
list_country= ['Brazil','China','India','Mexico','South Africa']
country_table1,year_val= tablefunc('urban_population.csv')
subplots(list_country)
heatmap('china.csv')

