import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    #Use Pandas to import the data from epa-sea-level.csv
    df_esl = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    #Use matplotlib to create a scatter plot using the Year column as the x-axis 
    # and the CSIRO Adjusted Sea Level column as the y-axis.


    # Create first line of best fit
    # Use the linregress function from scipy.stats to get the slope and y-intercept 
    # of the line of best fit. Plot the line of best fit over the top of the scatter plot. 
    # Make the line go through the year 2050 to predict the sea level rise in 2050.


    # Create second line of best fit
    # Plot a new line of best fit just using the data from year 2000 through the most recent year 
    # in the dataset. Make the line also go through the year 2050 to predict the sea level rise 
    # in 2050 if the rate of rise continues as it has since the year 2000.


    # Add labels and title
    # The x label should be Year, the y label should be Sea Level (inches), and the title 
    # should be Rise in Sea Level.

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()