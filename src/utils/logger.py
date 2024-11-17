import csv
from pathlib import Path

def log_data(file_path, temperature, soil_moisture, gas_resistance):
    """
    センサー値をCSVファイルに記録する
    Args:
        file_path (Path): ログファイルのパス
        temperature (float): 温度
        soil_moisture (float): 土壌水分
        gas_resistance (float): ガス抵抗
    """
    # ファイルが存在しない場合、ヘッダー行を追加して新規作成
    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)  # ディレクトリが存在しない場合は作成
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Temperature (°C)", "Soil Moisture (%)", "Gas Resistance (kΩ)"])

    # データを追記
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        from datetime import datetime
        writer.writerow([datetime.now().isoformat(), temperature, soil_moisture, gas_resistance])
