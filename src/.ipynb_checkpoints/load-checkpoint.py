import pandas as pd
import os

class Load:
    def __init__(self, dataframe, destiny_path, csv_name):
        self.dataframe = dataframe
        self.destiny_path = destiny_path
        self.csv_name = csv_name
        
    def load_to_csv(self):
        try:
            os.makedirs(self.destiny_path, exist_ok=True)  # Ensure directory exists
            self.dataframe.to_csv(os.path.join(self.destiny_path, self.csv_name), index=False)
            print(f"File saved successfully at {self.destiny_path}")
        except Exception as e:
            print(f"Error saving file {self.csv_name}: {e}")

