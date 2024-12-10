#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#GIS Plotting Project
#---The main objective of this script is to create statistical plots & figures based on user input.
#---User will provide the geodatabase and shapefile that they're using, in addition to 
#---what specific data they would like to plot from the shapefile. 
#---For the desired figure, the user will also input parameters for visualization purposes.


# In[ ]:


#import modules/libraries
import matplotlib.pyplot as plt
from matplotlib import style 
import geopandas as gpd
import fiona
import os
import numpy as np


# In[ ]:


#Import geodatabase using input
gdb_path = input(r"Insert geodatabase path: ")
print("Your geodatabase path: " , gdb_path)


# In[ ]:


#Listing Layers within gdb
layers = fiona.listlayers(gdb_path)
print("Layers in your gdb: ")
for shp in layers:
    print(shp) 


# In[ ]:


#listing all files in gdb
all_files = os.listdir(gdb_path)
print(all_files)


# In[ ]:


#List the available shapefiles in gdb and ask user which shp they'd like to use
shapefiles = []
for file in all_files:
    if file.endswith(('.shp','.SHP')):
        shapefiles.append(file)
print("Available shapefiles:")
for shp in shapefiles:
    print(shp)
input_shp = input("Insert shapefile: ")

#Provide info on shp path based on input
shp_path = os.path.join(gdb_path, input_shp)
print("Shapefile provided: " , input_shp)
print("Path of your shapefile: " , shp_path)


# In[ ]:


#Read shapefile given and list its columns
print("Shapefile provided: " , input_shp)
shp = gpd.read_file(shp_path)
col_list = []
for col in shp:
    col_list.append(col)
print("List of columns in " , input_shp)
for c in col_list:
    print(c)


# In[ ]:


#Prompt user to enter the plot they'd like to use.
print("Available Plots: ")
plot_list = ['Bar Graph', 'Scatter Plot', 'Histogram', 'Box Plot']
for p in plot_list:
    print(p)

input_figure = input("What plot would you like to use? ")
print("\n")

#List Plot Style Options for user
print("Available plot styles: ")
print("default")
for sty in plt.style.available: 
    print(sty)

#Prompt user to enter plot style
style = input("Enter a plot style: ")
plt.style.use(str(style))
if style == 'default':
    plt.rcParams.update(plt.rcParamsDefault)


# In[ ]:


#Bar Graph

if input_figure == 'Bar Graph':
    #Ask user for a vertical or horizontal bar graph.
    bar_graph_type = input("Vertical or Horizontal? ")
    if bar_graph_type == 'Vertical':
        #List columns again from shapefile to give options to the user on which columns to input
        print("List of columns in your shapefile: ")
        for c in col_list:
            print(c)
        input_col1 = input("Enter the 1st column you'd like to use [for the x-axis]: ")
        input_col2 = input("Enter the 2nd column you'd like to use [for the y-axis]: ")
        input_col1_list = []
        input_col2_list = []
        print("Columns to be used: " , input_col1, "and" , input_col2)
        
        #Append data from columns to lists
        for i, row in shp.iterrows():
            input_col1_list.append(row[input_col1])
            input_col2_list.append(row[input_col2])

        #User Input Parameters for Bar Graph Visualization
        input_range = input("Are you using a specific range of values from your list? (Type 'Yes or 'No'): ")
        #Ask user for range of values to be appended from their input columns
        if input_range == 'Yes':
            start_range = int(input("Enter your start value: "))
            end_range = int(input("Enter your end value: "))

            xAxis = input_col1_list[start_range: end_range + 1]
            yAxis = input_col2_list[start_range: end_range + 1]
            
            #Set width and height of figure
            graph_width = int(input("Width of your graph: "))
            graph_height = int(input("Height of your graph: "))
            
            #Labeling and set fontsizes
            graph_title = input("Add a title: ")
            fontsizeTitle = int(input("Enter fontsize of your title: "))
            labelX = input("Name your x-axis: ")
            fontsizeX = int(input("Enter fontsize of your x-axis name: "))
            labelY = input("Name your y-axis: ")
            fontsizeY = int(input("Enter fontsize of your y-axis name: "))

            #Plot bar graph
            fig, ax = plt.subplots(figsize=(graph_width, graph_height))
            plt.ticklabel_format(style='plain')
            plt.bar(xAxis, yAxis)
            plt.xlabel(labelX, fontsize = fontsizeX)
            plt.ylabel(labelY, fontsize = fontsizeY)
            plt.title(graph_title, fontsize = fontsizeTitle)
            #Display bar graph
            plt.show()     

        elif input_range == 'No':
            #Set width and height of figure
            graph_width = int(input("Width of your graph: "))
            graph_height = int(input("Height of your graph: "))
            
            #Labeling and set fontsizes
            graph_title = input("Add a title: ")
            fontsizeTitle = int(input("Enter fontsize of your title: "))
            labelX = input("Name your x-axis: ")
            fontsizeX = int(input("Enter fontsize of your x-axis name: "))
            labelY = input("Name your y-axis: ")
            fontsizeY = int(input("Enter fontsize of your y-axis name: "))

            #Plot bar graph
            fig, ax = plt.subplots(figsize=(graph_width, graph_height))
            plt.ticklabel_format(style='plain')
            plt.bar(input_col1_list, input_col2_list)
            plt.xlabel(labelX, fontsize = fontsizeX)
            plt.ylabel(labelY, fontsize = fontsizeY)
            plt.title(graph_title, fontsize = fontsizeTitle)
            #Display bar graph
            plt.show()
            
    elif bar_graph_type == 'Horizontal':
        #List columns again from shapefile to give options to the user on which columns to input
        print("List of columns in your shapefile: ")
        for c in col_list:
            print(c)
        input_col1 = input("Enter the 1st column you'd like to use [for the y-axis]: ")
        input_col2 = input("Enter the 2nd column you'd like to use [for the x-axis]: ")
        input_col1_list = []
        input_col2_list = []
        print("Columns to be used: " , input_col1, "and" , input_col2)
        
        #Append data from columns to lists
        for i, row in shp.iterrows():
            input_col1_list.append(row[input_col1])
            input_col2_list.append(row[input_col2])

        #User Input Parameters for Bar Graph Visualization
        input_range = input("Are you using a specific range of values from your list? (Type 'Yes or 'No'): ")
        #Ask user for range of values to be appended from their input columns
        if input_range == 'Yes':
            start_range = int(input("Enter your start value: "))
            end_range = int(input("Enter your end value: "))

            xAxis = input_col1_list[start_range: end_range + 1]
            yAxis = input_col2_list[start_range: end_range + 1]
            
            #Set width and height of figure
            graph_width = int(input("Width of your graph: "))
            graph_height = int(input("Height of your graph: "))
            
            #Labeling and set fontsizes
            graph_title = input("Add a title: ")
            fontsizeTitle = int(input("Enter fontsize of your title: "))
            labelX = input("Name your x-axis: ")
            fontsizeX = int(input("Enter fontsize of your x-axis name: "))
            labelY = input("Name your y-axis: ")
            fontsizeY = int(input("Enter fontsize of your y-axis name: "))

            #Plot bar graph
            fig, ax = plt.subplots(figsize=(graph_width, graph_height))
            plt.ticklabel_format(style='plain')
            plt.barh(xAxis, yAxis)
            plt.xlabel(labelX, fontsize = fontsizeX)
            plt.ylabel(labelY, fontsize = fontsizeY)
            plt.title(graph_title, fontsize = fontsizeTitle)
            #Display bar graph
            plt.show()     

        elif input_range == 'No':
            #Set width and height of figure
            graph_width = int(input("Width of your graph: "))
            graph_height = int(input("Height of your graph: "))
            
            #Labeling and set fontsizes
            graph_title = input("Add a title: ")
            fontsizeTitle = int(input("Enter fontsize of your title: "))
            labelX = input("Name your x-axis: ")
            fontsizeX = int(input("Enter fontsize of your x-axis name: "))
            labelY = input("Name your y-axis: ")
            fontsizeY = int(input("Enter fontsize of your y-axis name: "))

            #Plot bar graph
            fig, ax = plt.subplots(figsize=(graph_width, graph_height))
            plt.ticklabel_format(style='plain')
            x = input_col1_list
            y = input_col2_list
            plt.barh(x, y)
            plt.xlabel(labelX, fontsize = fontsizeX)
            plt.ylabel(labelY, fontsize = fontsizeY)
            plt.title(graph_title, fontsize = fontsizeTitle)
            #Display Bar Graph
            plt.show()


# In[ ]:


#Scatter Plot

if input_figure == 'Scatter Plot':
    #List columns again from shapefile to give options to the user on which columns to input
    print("List of columns in your shapefile: ")
    for c in col_list:
        print(c)
    input_col1 = input("Enter the 1st column you'd like to use [for your x-axis]: ")
    input_col2 = input("Enter the 2nd column you'd like to use [for your y-axis]: ")
    input_col1_list = []
    input_col2_list = []
    print("Columns to be used: " , input_col1, "and" , input_col2)
    for i, row in shp.iterrows():
        input_col1_list.append(row[input_col1])
        input_col2_list.append(row[input_col2])
        
    input_range = input("Are you using a specific range of values from your list? (Type 'Yes or 'No'): ")
    #Ask user for range of values to be appended from their input columns
    if input_range == 'Yes':
        start_range = int(input("Enter your start value: "))
        end_range = int(input("Enter your end value: "))
        
        xAxis = input_col1_list[start_range: end_range + 1]
        yAxis = input_col2_list[start_range: end_range + 1]
        
        #Set limits on axes
        lower_limit_x = int(input("Enter lower limit for the x-axis: "))
        upper_limit_x = int(input("Enter upper limit for the x-axis: "))    
        lower_limit_y = int(input("Enter lower limit for the y-axis: "))
        upper_limit_y = int(input("Enter upper limit for the y-axis: "))
        
        #Set width and height of figure
        graph_width = int(input("Width of your graph: "))
        graph_height = int(input("Height of your graph: "))
         
        #Labeling and set fontsizes
        graph_title = input("Add a title: ")
        fontsizeTitle = int(input("Enter fontsize of your title: "))
        labelX = input("Name your x-axis: ")
        fontsizeX = int(input("Enter fontsize of your x-axis name: "))
        labelY = input("Name your y-axis: ")
        fontsizeY = int(input("Enter fontsize of your y-axis name: "))
        
        #Create Scatter Plot   
        fig, ax = plt.subplots(figsize=(graph_width, graph_height))
        ax.set_xlim(lower_limit_x, upper_limit_x) 
        ax.set_ylim(lower_limit_y, upper_limit_y)
        plt.scatter(xAxis, yAxis)
        plt.ticklabel_format(style='plain')
        
        plt.xlabel(labelX, fontsize = fontsizeX)
        plt.ylabel(labelY, fontsize = fontsizeY)
        plt.title(graph_title, fontsize = fontsizeTitle)
        #Display Scatter Plot
        plt.show()
        
    elif input_range == 'No':
        #Set limits on axes
        lower_limit_x = int(input("Enter lower limit for the x-axis: "))
        upper_limit_x = int(input("Enter upper limit for the x-axis: "))    
        lower_limit_y = int(input("Enter lower limit for the y-axis: "))
        upper_limit_y = int(input("Enter upper limit for the y-axis: "))
         
        #Set width and height of figure
        graph_width = int(input("Width of your plot: "))
        graph_height = int(input("Height of your plot: "))
        
        #Labeling and set fontsizes
        graph_title = input("Add a title: ")
        fontsizeTitle = int(input("Enter fontsize of your title: "))           
        labelX = input("Name your x-axis: ")
        fontsizeX = int(input("Enter fontsize of your x-axis name: "))
        labelY = input("Name your y-axis: ")
        fontsizeY = int(input("Enter fontsize of your y-axis name: "))
        
        #Create scatter plot
        fig, ax = plt.subplots(figsize=(graph_width, graph_height))
        ax.set_xlim(lower_limit_x, upper_limit_x) 
        ax.set_ylim(lower_limit_y, upper_limit_y)
        x = input_col1_list
        y = input_col2_list
        plt.scatter(x, y)
        plt.ticklabel_format(style='plain')
        plt.xlabel(labelX, fontsize = fontsizeX)
        plt.ylabel(labelY, fontsize = fontsizeY)
        plt.title(graph_title, fontsize = fontsizeTitle)
        #Display Scatter Plot
        plt.show()


# In[ ]:


#Histogram

if input_figure == 'Histogram':
    #List columns again from shapefile to give options to the user on which columns to input
    print("List of columns in your shapefile: ")
    for c in col_list:
        print(c)
    input_column = input("Enter the column you'd like to use: ")
    input_column_list = []
    print("Column to be used: " , input_column)
    for i, row in shp.iterrows():
        input_column_list.append(row[input_column])
        
    #Ask user if they have bins for histogram visualization     
    input_bins = input("Do you have a list of bins? (Type 'Yes' or 'No'): ")
    if input_bins == 'Yes':
        #Provide bins, append each to a list (-1 to stop asking for input)
        bins_list = []
        i = 0
        while i != -1:
            i = int(input("Add a number to your bin list (-1 to stop): "))
            if i != -1:
                bins_list.append(i)
            elif i == -1:
                break
                
        #Set width and height of figure     
        graph_width = int(input("Width of your plot: "))
        graph_height = int(input("Height of your plot: "))
        
        #Labeling and set fontsizes 
        graph_title = input("Add a title: ")
        fontsizeTitle = int(input("Enter fontsize of your title: "))           
        labelX = input("Name your x-axis: ")
        fontsizeX = int(input("Enter fontsize of your x-axis name: "))
        labelY = input("Name your y-axis: ")
        fontsizeY = int(input("Enter fontsize of your y-axis name: "))

        #Create histogram
        fig, ax = plt.subplots(figsize=(graph_width, graph_height))
        plt.ticklabel_format(style='plain')
        plt.hist(input_column_list, bins= bins_list, edgecolor = 'black')
        plt.xlabel(labelX, fontsize = fontsizeX)
        plt.ylabel(labelY, fontsize = fontsizeY)
        plt.title(graph_title, fontsize = fontsizeTitle)
        #Display histogram
        plt.show()
        
    if input_bins == 'No':
        #Ask user for number of bins the script will add to the histogram (if they don't have their own bins)
        num_bins = int(input("Enter the number of bins: "))
        
        #Set width and height of figure
        graph_width = int(input("Width of your plot: "))
        graph_height = int(input("Height of your plot: "))
        
        #Labeling and set fontsizes
        graph_title = input("Add a title: ")
        fontsizeTitle = int(input("Enter fontsize of your title: "))           
        labelX = input("Name your x-axis: ")
        fontsizeX = int(input("Enter fontsize of your x-axis name: "))
        labelY = input("Name your y-axis: ")
        fontsizeY = int(input("Enter fontsize of your y-axis name: "))

        #Create histogram
        fig, ax = plt.subplots(figsize=(graph_width, graph_height))
        plt.ticklabel_format(style='plain')
        plt.hist(input_column_list, bins= num_bins, edgecolor = 'black')
        plt.xlabel(labelX, fontsize = fontsizeX)
        plt.ylabel(labelY, fontsize = fontsizeY)
        plt.title(graph_title, fontsize = fontsizeTitle)
        # Display histogram
        plt.show()


# In[ ]:


#Box Plot
if input_figure == 'Box Plot':
    #Create data list to be appended and used for plotting
    data = []
    #List columns again from shapefile to give options to the user on which columns to input
    num_columns = int(input("Enter the number of columns you'd like to use: "))
    for i in range(num_columns):
        print("List of columns in your shapefile: ")
        for c in col_list:
            print(c)
        input_column_list = []
        input_column = input("Enter a column: ")
        print("Column " , i + 1, ":" , input_column)
        for i, row in shp.iterrows():
            input_column_list.append(row[input_column])
        data.append(input_column_list)       

    #Set width and height of figure
    graph_width = int(input("Width of your graph: "))
    graph_height = int(input("Height of your graph: "))
    
    #Labeling and set fontsizes
    graph_title = input("Enter a title: ")  
    fontsizeTitle = int(input("Enter fontsize of your title: "))           
    labelX = input("Name your x-axis: ")
    fontsizeX = int(input("Enter fontsize of your x-axis name: "))
    labelY = input("Name your y-axis: ")
    fontsizeY = int(input("Enter fontsize of your y-axis name: "))

    #Create box plot
    fig, ax = plt.subplots(figsize=(graph_width, graph_height))
    ax.set_xlabel(labelX, fontsize = fontsizeX)
    ax.set_ylabel(labelY, fontsize = fontsizeY)
    plt.title(graph_title, fontsize = fontsizeTitle)
    plt.boxplot(data)
    #Tick labeling
    ticks_list = []
    tick_labels = []
    for i in range(num_columns):
        ticks_list.append(i+1)
        tick_label = input("Label your tick: ")
        tick_labels.append(tick_label)
    plt.xticks(ticks_list, tick_labels)
    #Display boxplot
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




