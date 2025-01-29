from data_collector import KaggIn as ki

dataset_ref = "sudalairajkumar/cryptocurrencypricehistory"
collect_data = ki(dataset_ref)
collect_data.collect()
