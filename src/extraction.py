import pandas as pd

class Extract:
    def __init__(self, file_to_process):
        self.file_to_process = file_to_process

    def extract_from_csv(self):
        try:
            dataframe = pd.read_csv(self.file_to_process, encoding_errors='ignore')
            return dataframe
            
        except Exception as e:
            print(f"Error reading {self.file_to_process}: {e}")
            return None