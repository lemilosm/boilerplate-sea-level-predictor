import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    #Use Pandas to import the data from epa-sea-level.csv
    df_esl = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #Use matplotlib to create a scatter plot using the Year column as the x-axis 
    # and the CSIRO Adjusted Sea Level column as the y-axis.
    fig, ax = plt.subplots(figsize=(6,4))
    x = df_esl["Year"].to_numpy()
    y = df_esl["CSIRO Adjusted Sea Level"].to_numpy()
    ax.scatter(x, y)
    ax.set(title='Rise in Sea Level', xlabel='Year', ylabel='Sea Level (inches)',
            xticks=[1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    # plt.show()

    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept 
    # of the line of best fit. Plot the line of best fit over the top of the scatter plot. 
    # Make the line go through the year 2050 to predict the sea level rise in 2050.
   
    # linear regression parametters
    linearreg = linregress(x, y)
    # obtaining pred line to plot it
    y_pred = x * linearreg.slope + linearreg.intercept
    # prediction of sea level from 2014 to 2050
    y_2014to2050 = []
    for i,yr in enumerate(range( x[-1]+1 ,2051 )):
        y_2014to2050.append(yr * linearreg.slope + linearreg.intercept)
        # print(i,yr)

    # extending pred line to year 2050 (year by year), and also its correspondind x array
    y_pred2050 = np.append(y_pred, y_2014to2050)  
    x_2050 = np.append(x ,   range( x[-1]+1 ,2051 ) )

    # plotting
    # ax.scatter(x, y)
    ax.plot(x_2050 , y_pred2050 , 'r' )


    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year 
    # in the dataset. Make the line also go through the year 2050 to predict the sea level rise 
    # in 2050 if the rate of rise continues as it has since the year 2000.

    # 2nd pred line subset
    x_since_2000 = x[ np.where(x>=2000)[0][0] : ]
    y_since_2000 = y[ np.where(x>=2000)[0][0] : ]

    # getting new prediction lin reg params
    linearreg_since_2000 = linregress(x_since_2000, y_since_2000)

    # predicting 2000 to 2050

    y_pred_2000to2050 = []
    for i,yr in enumerate(range( 2000 ,2051 )):
        y_pred_2000to2050.append(yr * linearreg_since_2000.slope + linearreg_since_2000.intercept)

    ax.plot( range( 2000 ,2051 ) , y_pred_2000to2050 , 'g' )

    # Add labels and title
    # The x label should be Year, the y label should be Sea Level (inches), and the title 
    # should be Rise in Sea Level.
    
    # already done above at the first plotting, but, investigated how to add a label for each line
    
    ax.legend(['datapoints', 'Linear Regression since 1880', 'Linear Regression since 2000'])

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()