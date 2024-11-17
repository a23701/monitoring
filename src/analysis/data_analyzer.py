import pandas as pd

def calculate_statistics(file_path):
    """
    CSVファイルからデータを読み取り、統計量を計算する関数
    Args:
        file_path: データが保存されたCSVファイルのパス
    Returns:
        各センサーの統計量 (平均、最大、最小など)
    """
    data = pd.read_csv(file_path)

    stats = {
        "Temperature": {
            "mean": data['Temperature (°C)'].mean(),
            "max": data['Temperature (°C)'].max(),
            "min": data['Temperature (°C)'].min(),
        },
        "Soil Moisture": {
            "mean": data['Soil Moisture (%)'].mean(),
            "max": data['Soil Moisture (%)'].max(),
            "min": data['Soil Moisture (%)'].min(),
        },
        "Gas Resistance": {
            "mean": data['Gas Resistance (kΩ)'].mean(),
            "max": data['Gas Resistance (kΩ)'].max(),
            "min": data['Gas Resistance (kΩ)'].min(),
        },
    }
    return stats
