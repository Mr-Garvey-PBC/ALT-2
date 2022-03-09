# MAke sure .csv is in the same folder as the python file

import pandas # Import pandas module so you can use its features

file_data=pandas.read_csv('01. cod.csv')   # Read and open your csv file, dont forget to put the .csv after your file name
#print(file_data)                      # Can run a print statement here to see that your data has loaded.

cod_df=pandas.DataFrame(file_data)     # Create a dataframe using the data you uploaded in line 3 and assign it to a variable
                                       # Assigning the data to a variable like cod_df makes it easier to manipulate data as the program evolves.
                                       # You are using .DataFrame to create a dataframe from the information withing file_data
                                       # Capital D and F for the word DataFrame

#print(cod_df)                         # Print statement to see dataframe has loaded data. You will see the data is truncated (only some is shown)
#print(cod_df.to_string())             # Use the .to_string() method to see ALL the data. (not really necessary)
print(cod_df.info())                   # Show user all the column headings and data type int64=int, float64=float, object64=string

# Create a new dataframe containing just the data you want for your analysis
new_cod_df=cod_df[['wins','kdRatio','level']]   # Created a new dataframe from the data contained within the original dataframe.

# Columns selected for the new datafame are entered as individual strings, and must match exactly what is written in the datafrrame
# i.e Wins and wins are two different things because of the capital w. Column headings must also be within double square brackets.

print(new_cod_df.sort_values('wins',ascending=False).head(10))  # Sort top 10 values using .head(10), try changing number within brackets.

# Basic Data analysis
print('\n',new_cod_df.mean())          # Find the mean of each column
#print('\n',new_cod_df.describe()) 