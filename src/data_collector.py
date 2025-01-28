import kagglehub

# Download latest version
path = kagglehub.dataset_download("sudalairajkumar/cryptocurrencypricehistory")

print("Path to dataset files:", path)