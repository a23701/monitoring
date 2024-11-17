import pandas as pd
from pathlib import Path
from datetime import datetime
from alert_notifier import send_alert  # メール通知機能をインポート

DATA_FILE = Path("/home/kon/monitoring/data/sensor_data.csv")
LOG_FILE = Path("/home/kon/monitoring/logging.log")

def evaluate_maturity(data):
    latest_data = data.iloc[-1]
    temperature = latest_data["Temperature (°C)"]
    soil_moisture = latest_data["Soil Moisture (%)"]
    gas_resistance = latest_data["Gas Resistance (kΩ)"]

    if temperature > 50:
        send_alert("異常アラート: 温度が高すぎます", f"現在の温度: {temperature}°C")
    if soil_moisture < 20:
        send_alert("異常アラート: 土壌水分が低すぎます", f"現在の土壌水分: {soil_moisture}%")
    if gas_resistance < 2.0:
        send_alert("異常アラート: ガス濃度が高すぎます", f"現在のガス抵抗: {gas_resistance}kΩ")

    if temperature <= 40 and 40 <= soil_moisture <= 60 and gas_resistance >= 5.0:
        return "成熟段階"
    elif 40 < temperature <= 50 or 2.0 <= gas_resistance < 5.0:
        return "中間段階"
    else:
        return "初期段階"

def main():
    if not DATA_FILE.exists():
        print(f"データファイルが見つかりません: {DATA_FILE}")
        return

    data = pd.read_csv(DATA_FILE)
    maturity_status = evaluate_maturity(data)

    with open(LOG_FILE, mode="a", newline="") as file:
        timestamp = datetime.now().isoformat()
        file.write(f"{timestamp}, 判定結果: {maturity_status}\n")
        print(f"{timestamp}, 判定結果: {maturity_status}")

if __name__ == "__main__":
    main()
