
# coding: utf-8

# In[142]:


# Import Dependencies
import os
import csv
import random
import string
import pandas as pd


# In[143]:


# Reference the file where the CSV is located
financial_csv_path = "budget_data.csv"


# In[144]:


# Import the data into a Pandas DataFrame
financial_df = pd.read_csv(financial_csv_path, encoding="ISO-8859-1")


# In[145]:


with open(financial_csv_path, newline='') as csvfile:

   # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

   # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

   # Read each row of data after the header
    for row in csvreader:
        print(row)


# In[146]:


row_count = 0
with open(financial_csv_path, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #row_count = row_count + 1
    
    #print(csvreader)
     
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        row_count = row_count + 1
       


# In[147]:


financial_df


# In[149]:


total_profit_losses = financial_df["Profit/Losses"].sum()  
financial_df['shifted_column'] = financial_df["Profit/Losses"].shift(1)
financial_df['difference'] = financial_df["Profit/Losses"]-financial_df['shifted_column']
financial_df['difference'] = financial_df['difference'].abs()
faverage = financial_df['difference'].mean(axis=0)
#fmaximum = financial_df['difference'].max()
#fminumum = financial_df['difference'].min()
financial_df[financial_df["Profit/Losses"]==financial_df["Profit/Losses"].max()]


# In[150]:


financial_df[financial_df["Profit/Losses"]==financial_df["Profit/Losses"].min()]


# In[151]:
tmonths=str(row_count)
tprofits=str(total_profit_losses)
taverage=str(faverage)
maxprofit=str(financial_df["Profit/Losses"].max())
minprofit=str(financial_df["Profit/Losses"].min())

# Capture Report Info
Title="Financial Analysis"
Line0="_______________________________________________________________"
#Line1="Total Months: " + str(row_count))
Line1="Total Months: " + tmonths

#Line2="Total Profit/Losses: $" + str(total_profit_losses))
Line2="Total Profit/Losses: $" + tprofits

#Line3="Average Change: $" + str(faverage))
Line3="Average Change: $" + taverage

#print("Greatest Increase in Profits: $" + str(maximum))
#Line4="Greatest Increase in Profits: $" + str(financial_df["Profit/Losses"].max()))
Line4="Greatest Increase in Profits: $" + maxprofit

#print("Greatest Decrease in Profits: $" + str(minimum))
#Line5="Greatest Decrease in Profits: $" + str(financial_df["Profit/Losses"].min()))
Line5="Greatest Decrease in Profits: $" + minprofit

# Print to screen
print("Financial Analysis")
print("_______________________________________________________________")
print("Total Months: " + str(row_count))
print("Total Profit/Losses: $" + str(total_profit_losses))
print("Average Change: $" + str(faverage))
#print("Greatest Increase in Profits: $" + str(maximum))
print("Greatest Increase in Profits: $" + str(financial_df["Profit/Losses"].max()))
#print("Greatest Decrease in Profits: $" + str(minimum))
print("Greatest Decrease in Profits: $" + str(financial_df["Profit/Losses"].min()))



# Print to file
DataPrint=open(r"C:\Users\kimberly\Desktop\GTATL201808DATA3-master\03-Python\PyBank_Gordon_Results.csv","w")
DataPrint.write(f'{Title}\n')
DataPrint.write(f'{Line0}\n')
DataPrint.write(f'{Line1}\n')
DataPrint.write(f'{Line2}\n')
DataPrint.write(f'{Line3}\n')
DataPrint.write(f'{Line4}\n')
DataPrint.write(f'{Line5}\n')
DataPrint.close()






    


# In[ ]:





# In[ ]:




