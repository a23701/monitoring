import csv
from datetime import datetime

def log_data(file_path, temperature, soil_moisture, gas_resistance):
    """
    センサー値をCSVファイルに記録する関数
    Args:
        file_path: 保存先のCSVファイルパス
        temperature: 温度センサーの値
        soil_moisture: 土壌水分センサーの値
        gas_resistance: MQ135ガスセンサーの値
    """
    # ヘッダー行を記録
    if not file_path.exists():
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Temperature (°C)", "Soil Moisture (%)", "Gas Resistance (kΩ)"])

    # データを追記
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, temperature, soil_moisture, gas_resistance])
