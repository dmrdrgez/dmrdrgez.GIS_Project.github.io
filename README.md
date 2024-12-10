# Adv. GIS Project: Creating Statistical Figures Based on User Input

![image](https://github.com/user-attachments/assets/42c62161-5bc3-4d02-b135-51af54ba605f)


## About the Project
- This project creates statistical plots based on information provided by the user with the use of Geopandas open source and the Matplotlib library. The script is designed for users working with geodatabases and shapefiles in GIS who may want to complement their spatial anaylsis with other statistical visualizations.

## Importance of Statistics Visualization
- Identifying trends or relationships: Statistical figures help researchers observe trends or lack thereof based on discernible patterns. 
- Corroboration of findings: These data visualizations provide additional support to researchers when validating their findings (quality control).
- Communication tool for the target audience: Statistical plots are utlitized as messaging tools and are a key resource when communicating an issue to the public. 
- Simplifying complex datasets: Visualization helps to 'clean' the data, making it more concise and tangible.


## Features of the Tool
- User input-based script allows for customization of statistical figures for better visualization. 
- Options to create four statistical plots: bar graphs (vertical and horizontal), scatter plots, histograms, and box plots (single and multiple plots).
- Code provides options and information to the user in order to facilitate input.
- Produces easy-to-read figures which can be integrated into anaylsis projects.

## [Link to Full Repository](https://github.com/dmrdrgez/dmrdrgez.GIS_Project.github.io)

## Code Snippets

**Choosing Plot Type and Style**
```
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
```

**Creating a Histogram**

```
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
```


**Creating a Box Plot**

```
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
```

## Sample Statistical Plots

**Box Plot**

![image](https://github.com/user-attachments/assets/14cbc0c1-d643-42b8-bbdb-3db136dbd215)

**Bar Graph**

![image](https://github.com/user-attachments/assets/3643e859-3a85-4d80-a338-120af1af93a5)

**Scatter Plot**

![image](https://github.com/user-attachments/assets/0ef42272-85f1-4134-a752-f87ed0dfc87f)

**Histogram**

![image](https://github.com/user-attachments/assets/88090c85-4d9a-4745-a013-5b8f9b986b74)





