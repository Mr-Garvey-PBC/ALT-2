import pandas # Import pandas module so you can use its features
#import matplotlib.pyplot as plt

file_data=pandas.read_csv('best_in_show2.csv')   # Read and open your csv file, dont forget to put the .csv after your file name
#print(file_data)                               # Can run a print statement here to see that your data has loaded.

All_data_df=pandas.DataFrame(file_data)     # Create a dataframe using the data you uploaded in line 3 and assign it to a variable
                                            # Assigning the data to a variable like cod_df makes it easier to manipulate data as the program evolves.
                                            # You are using .DataFrame to create a dataframe from the information withing file_data
                                            # Capital D and F for the word DataFrame

#print(All_data_df)                         # Print statement to see dataframe has loaded data. You will see the data is truncated (only some is shown)
#print(All_data_df.to_string())             # Use the .to_string() method to see ALL the data. (not really necessary)
print(All_data_df.info())                   # Show user all the column headings and data type int64=int, float64=float, object64=string

# Create a new dataframe containing just the data you want for your analysis Genetic diseases
specific_data_df=All_data_df[['Dog breed','category','GENETIC DISEASES - congenital ailments: summary / areas affected']]   # Created a new dataframe from the data contained within the original dataframe.
# print(specific_data_df.to_string())
# #specific_data_df.rename(columns=({'GENETIC DISEASES - congenital ailments: summary / areas affected':'Genetic Disease'}))
# 
hip_problems=specific_data_df[specific_data_df['GENETIC DISEASES - congenital ailments: summary / areas affected']=='hip problems']
#hip_problems=specific_data_df[specific_data_df['GENETIC DISEASES - congenital ailments: summary / areas affected'].str.contains('hip problems',na=False)]
print(hip_problems.to_string())
print('\n',hip_problems['category'].value_counts())

# Remove blank or Na values and change data type
# cost_df=All_data_df[['category','LONGEVITY']]
# #print(cost_df)
# cost_df=cost_df.dropna()
# cost_df['LONGEVITY']=cost_df['LONGEVITY'].str.replace(r'%','')
# cost_df['LONGEVITY']=cost_df['LONGEVITY'].astype(int, errors='ignore')
# #input()
# #print(cost_df.mean())
# 
# # Mean algorithm
# # print(cost_df.loc[cost_df['category']=='sporting','LONGEVITY'].mean())
# # print(cost_df.loc[cost_df['category']=='working','LONGEVITY'].mean())
# # print(cost_df.loc[cost_df['category']=='hound','LONGEVITY'].mean())
# #print(cost_df.to_string())
# #print(cost_df.info())
# 
# long_list=cost_df['LONGEVITY'].tolist()
# print(long_list)
# sum_of_list=sum(long_list)
# average=sum_of_list/len(long_list)
# print('Average life span of a dog is',average)