import pandas as pd

#Read the data from the CSV file inside the zip
df = pd.read_csv("data/winemag-data-130k-v2.csv.zip")



#Group the data by 'country', count 'reviews', and calculate average points
summary_df = df.groupby('country').agg(
     count = ('country', 'size'), # count the number of reviews
     points = ('points', 'mean')).reset_index() # calculate the average points

#Round the 'points' column to 1 decimal point
summary_df['points'] = summary_df['points'].round(1)

#write the summary data to a new csv file 
summary_df.to_csv('data/reviews-per-country.csv', index=False)

print('summary CSV file is created successfully')

