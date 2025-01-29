#import libraries
#!pip install kaggle
import os
import zipfile

class KaggIn():
    def __init__(self, dataset_ref):
        self.dataset_ref = dataset_ref
        
        #source zip file with data
        self.zip_name = "cryptocurrencypricehistory.zip"
        
        #resulting extracted folder name
        self.extract_folder = "my_dataset"
        
    def collect(self):
        #download dataset via Command Line
        os.system(f"kaggle datasets download -d {self.dataset_ref}")
        
        # Extract files from ZIP
        with zipfile.ZipFile(self.zip_name, "r") as zip_ref:
            zip_ref.extractall(self.extract_folder)
            
        # List extracted files
        file_list = os.listdir(self.extract_folder)
        print("Extracted files:", file_list)
