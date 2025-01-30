# import lybraries
import pandas as pd
from data_collector import Collector
from extraction import Extract
from transformations import Transform
from load import Load
import glob
import os

# Collect Data from Kaglle API
dataset_ref = "sudalairajkumar/cryptocurrencypricehistory"
collect_data = Collector(dataset_ref)
collect_data.collect()

# specify the origin(i) and destiny(f) paths
i_path = "C:/Users/Utilizador/GoogleDrive/Portfolio/Bitcoin_Data-Engineering-Project/src/my_dataset"
f_path = "C:/Users/Utilizador/GoogleDrive/Portfolio/Bitcoin_Data-Engineering-Project/product"

# creat a list with the name of all csv files
files = glob.glob(f"{i_path}/*.csv")

# run ETL Pipeline
for file in files:
    #Extract
    extract = Extract(file)
    df = extract.extract_from_csv()

    if df is not None:
        #Transform
        transform = Transform(df)
        transformed_df = transform.split_Date()
        
        #Load
        csv_name = os.path.basename(file)  # Extract file name
        load_df = Load(transformed_df, f_path, csv_name)
        load_df.load_to_csv()
   
    else:
        print(f"Skipping transformation and loading for {file} due to extraction failure.")

