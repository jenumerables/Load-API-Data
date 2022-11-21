#Load API Data to SQL Server Using Python
# Importing modules import requests. install requests and pandas prior to running.
import requests
import pandas as pd 
from pandas import json_normalize

# Defininig headers
headers = {
    'accept':'application/json',
}

# Defining baseurl
baseurl = 'https://jsonplaceholder.typicode.com/'
# defining endpoint
endpoint = 'users'

# Main request function
def main_request(baseurl,endpoint,headers):
    #using request to call API data
    r = requests.get(baseurl + endpoint, headers=headers)
    #returning data in json format
    return r.json()

# Variable calling main function
data = main_request(baseurl=baseurl,endpoint=endpoint,headers=headers)
#creating a dataframe
data_DF = pd.DataFrame(data)
#print out data
#print(data_DF)
# Add code to fix the nested JSON structure.

# Adding a column called index to data_DF dataframe 
data_DF['index'] = range(0, len(data_DF))

# Create a different dataframe for the nested column
company_DF = pd.concat([pd.DataFrame(json_normalize(x)) for x in data_DF['company']],sort=False)
# Rename the column names to include the company prefix
company_DF.columns = 'company_' + company_DF.columns
# Add a new column to company_df dataframe
company_DF['index'] = range(0, len(company_DF))

# Combine data_DF dataframe with company_DF dataframe with nested column
merged_DF = pd.merge(data_DF, company_DF, on='index')
# Dropping address column
merged_DF = merged_DF.drop(['address'], axis=1)
# Dropping the company
merged_DF = merged_DF.drop(['company'], axis=1)

# Print merged data
print(merged_DF)

