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
    return(country_table,year_table)

def multiline_plot(country):
    """
    This function takes a list of G7 countries(Canada, France, Germany, Italy,
    Japan, UK, USA) and plots the percentage
    of urban population over the years (with a step of 5 years)
    """
    #to get a list of years with a step of 5 years
    year = [val for val in list(country_table1.columns.values) if val.isdigit()]
    year= year[-1::-5]
    year_5= year[::-1]
    #creating new dataframe with data from the selected countries and years
    new_data= country_table1.loc[country][year_5]
    plt.rcParams["figure.figsize"] = (10,7)
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
    print('table for the difference between the max and min percentage')
    print(year_table1[country].max()-year_table1[country].min())

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
    fig, ax = plt.subplots(figsize=(7,5))
    ax.imshow(final_data)
    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(label)), labels=label)
    ax.set_yticks(np.arange(len(label)), labels=label)
    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=15, ha="right")
    for i,value in enumerate(label): #loop to add correlation value to the heatmap
        for j in range(len(label)):
            ax.text(j,i,round(final_data[value][j],3),ha="center", va="center", color="r")       
    #to get the country name inorder to set the title of the heatmap
    ax.set_title(data['Country Name'][0])
    fig.tight_layout() 
    plt.savefig(data['Country Name'][0])
    plt.show()
    
def bar_graph():
    """
    This function plots two graphs for the G7 countries(given in list_country):
        1. agricultural NO2 emission between(1999-2019)
        2. agricultural methane emission between(1999-2019)
    """
    data= pd.read_csv('agri_no2.csv',skiprows=4)
    year90_99= ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999']
    year00_09= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009']
    year10_19= ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
    data= data.loc[data['Country Name'].isin(list_country)]
    data['1990-1999']= data[year90_99].mean(axis=1)
    data['2000-2009']= data[year00_09].mean(axis=1)
    data['2010-2019']= data[year10_19].mean(axis=1)
    year=['1990-1999','2000-2009','2010-2019']
    #plotting bar graph for agricultural NO2 emission
    data.plot(kind='bar',x='Country Name',y= year,rot=15,align='center')
    plt.ylabel('NO2 emission(1000 metric ton CO2 equivalent)')
    plt.title('Agricultural NO2 emission (1999-2019)')
    plt.savefig('agri_NO2')
    data1= pd.read_csv('agri_methane.csv',skiprows=4)
    data1= data1.loc[data1['Country Name'].isin(list_country)]
    data1['1990-1999']= data1[year90_99].mean(axis=1)
    data1['2000-2009']= data1[year00_09].mean(axis=1)
    data1['2010-2019']= data1[year10_19].mean(axis=1)
    #plotting bar graph for agricultural methane emission
    data1.plot(kind='bar',x='Country Name',y= year,rot=15,align='center')
    plt.ylabel('Methane emission(1000 metric ton CO2 equivalent)')
    plt.title('Agricultural methane emission (1999-2019)')
    plt.savefig('agri_methane')
    plt.show()

def subplots():
    """
    This function plots 8 subplots for the change in agriculture land area
    in the G7 countries and the world between 1965 and 2020 (with a step of 5 years)
    """
    #creating a new list with the G7 countries and world
    country=list_country.copy()
    country.append('World')
    year = [val for val in list(country_table1.columns.values) if val.isdigit()]
    #to get a list of years with a step of 5 years
    year= year[-2::-5]
    year_5= year[-2::-1]
    #creating new dataframe with data from the selected countries and years
    new_data= country_table2.loc[country][year_5]
    fig, axs = plt.subplots(2, 4, figsize=(20, 10))
    for ind,name in enumerate(country): #loop for plotting the 8 subplots
        plt.subplot(2,4,ind+1)
        plt.plot(new_data.loc[name],label=name)
        plt.legend()
        plt.xticks(rotation=45.0)
        plt.title('Agricultural Land in sq km')
    plt.savefig('subplots8')
    plt.show()
    #creating table to show the average change in area each year between 1965 and 2020
    print('table to show the avg change in area between each year')
    print(year_table2[country].std())

list_country=['Canada','France','Germany','Italy','Japan',
              'United Kingdom','United States']
country_table1,year_table1= tablefunc('urban_population.csv')
country_table2,year_table2= tablefunc('agri_land_km.csv') 
multiline_plot(list_country)
bar_graph()
subplots()
heatmap('United States.csv')
heatmap('Japan.csv')
