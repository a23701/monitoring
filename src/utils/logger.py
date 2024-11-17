import csv
from datetime import datetime

def log_data(file_name, temperature, soil_moisture, gas_resistance):
    """
    センサー値をCSVファイルに記録する関数
    """
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, temperature, soil_moisture, gas_resistance])
