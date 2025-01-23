import csv
from datetime import datetime

def log_data(file_path, temperature, soil_moisture, gas_resistance, dht_temp, dht_humidity):
    """
    CSVファイルにデータを記録
    Args:
        file_path (Path): CSVファイルのパス
        temperature (float): 温度
        soil_moisture (float): 土壌水分
        gas_resistance (float): ガス抵抗
        dht_temp (float): DHT11温度
        dht_humidity (float): DHT11湿度
    """
    file_exists = file_path.exists()
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # ヘッダーを書き込む
            writer.writerow(["Timestamp", "Temperature (°C)", "Soil Moisture (%)", "Gas Resistance (kΩ)", "DHT Temperature (°C)", "DHT Humidity (%)"])
        writer.writerow([datetime.now().isoformat(), temperature, soil_moisture, gas_resistance, dht_temp, dht_humidity])
