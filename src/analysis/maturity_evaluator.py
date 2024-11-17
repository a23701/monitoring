import pandas as pd
from pathlib import Path
from datetime import datetime

# データファイルのパス
DATA_FILE = Path("/home/kon/monitoring/data/sensor_data.csv")
LOG_FILE = Path("/home/kon/monitoring/logging.log")

def evaluate_maturity(data):
    """
    コンポストの成熟度を判定する
    Args:
        data (DataFrame): センサーデータ
    Returns:
        str: 判定結果（初期段階, 中間段階, 成熟段階）
    """
    # 最新データを取得
    latest_data = data.iloc[-1]
    temperature = latest_data["Temperature (°C)"]
    soil_moisture = latest_data["Soil Moisture (%)"]
    gas_resistance = latest_data["Gas Resistance (kΩ)"]

    # 判定基準
    if temperature > 50 or gas_resistance < 2.0:
        return "初期段階"
    elif 40 < temperature <= 50 or 2.0 <= gas_resistance < 5.0:
        return "中間段階"
    elif temperature <= 40 and 40 <= soil_moisture <= 60 and gas_resistance >= 5.0:
        return "成熟段階"
    else:
        return "未判定"

def log_maturity_status(status):
    """
    判定結果をログファイルに記録
    Args:
        status (str): 判定結果
    """
    with open(LOG_FILE, mode="a", newline="") as file:
        timestamp = datetime.now().isoformat()
        file.write(f"{timestamp}, 判定結果: {status}\n")
        print(f"{timestamp}, 判定結果: {status}")

def main():
    if not DATA_FILE.exists():
        print(f"データファイルが見つかりません: {DATA_FILE}")
        return

    # データを読み込む
    data = pd.read_csv(DATA_FILE)

    # 成熟度判定
    maturity_status = evaluate_maturity(data)

    # ログに記録
    log_maturity_status(maturity_status)

if __name__ == "__main__":
    main()
