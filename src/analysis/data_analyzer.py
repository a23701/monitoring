import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# CSVファイルのパス
DATA_FILE = Path("/home/kon/monitoring/data/sensor_data.csv")

def analyze_data():
    # CSVデータを読み込む
    if not DATA_FILE.exists():
        print(f"データファイルが見つかりません: {DATA_FILE}")
        return

    data = pd.read_csv(DATA_FILE)

    # 基本統計量の計算
    print("データの基本統計量:")
    print(data.describe())

    # 各項目の平均値、最大値、最小値
    print(f"温度 (°C) 平均: {data['Temperature (°C)'].mean()}, 最大: {data['Temperature (°C)'].max()}, 最小: {data['Temperature (°C)'].min()}")
    print(f"土壌水分 (%) 平均: {data['Soil Moisture (%)'].mean()}, 最大: {data['Soil Moisture (%)'].max()}, 最小: {data['Soil Moisture (%)'].min()}")
    print(f"ガス抵抗 (kΩ) 平均: {data['Gas Resistance (kΩ)'].mean()}, 最大: {data['Gas Resistance (kΩ)'].max()}, 最小: {data['Gas Resistance (kΩ)'].min()}")

    # データの可視化
    data.plot(x="Timestamp", y=["Temperature (°C)", "Soil Moisture (%)", "Gas Resistance (kΩ)"], subplots=True, figsize=(10, 8))
    plt.savefig("/home/kon/monitoring/output/data_analysis_plot.png")
    plt.show()

if __name__ == "__main__":
    analyze_data()
