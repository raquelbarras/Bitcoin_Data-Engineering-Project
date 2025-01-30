#import lybraries
import pandas as pd

class Transform():
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def split_Date(self):
        if "Date" in self.dataframe.columns:
            #change from object to datetime format
            self.dataframe["Date"] = pd.to_datetime(self.dataframe["Date"])

            #Split the content of Date column into separate data and time columns
            self.dataframe["date"] = self.dataframe["Date"].dt.date 
            self.dataframe["time"] = self.dataframe["Date"].dt.time
        
            #Drop the original Date Column
            self.dataframe.drop(columns=["Date"], inplace=True)

        else:
            print("Column 'Date' not found in dataframe")
            
        return self.dataframe
        
            
        
