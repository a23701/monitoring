from flask import Flask, render_template
from utils.compost_status import get_compost_status
import pandas as pd
import os

app = Flask(__name__)

DATA_FILE = "/home/kon/monitoring/data/sensor_data.csv"

@app.route("/")
def dashboard():
    # データ読み込み
    if os.path.exists(DATA_FILE):
        data = pd.read_csv(DATA_FILE)
        recent_data = data.tail(10)
        temperature = recent_data["Temperature (°C)"].tolist()
        soil_moisture = recent_data["Soil Moisture (%)"].tolist()
        gas_resistance = recent_data["Gas Resistance (kΩ)"].tolist()
        timestamps = recent_data["Timestamp"].tolist()

        # 最新データでコンポスト状況を取得
        latest_data = recent_data.iloc[-1]
        compost_status = get_compost_status(
            latest_data["Temperature (°C)"],
            latest_data["Soil Moisture (%)"],
            latest_data["Gas Resistance (kΩ)"]
        )
    else:
        temperature = soil_moisture = gas_resistance = timestamps = []
        compost_status = "データがありません"

    return render_template(
        "dashboard.html",
        temperature=temperature,
        soil_moisture=soil_moisture,
        gas_resistance=gas_resistance,
        timestamps=timestamps,
        compost_status=compost_status
    )

def dashboard():
    if os.path.exists(DATA_FILE):
        data = pd.read_csv(DATA_FILE)
        recent_data = data.tail(10)
        temperature = recent_data["Temperature (°C)"].tolist()
        soil_moisture = recent_data["Soil Moisture (%)"].tolist()
        gas_resistance = recent_data["Gas Resistance (kΩ)"].tolist()
        timestamps = recent_data["Timestamp"].tolist()

        # 最新データでコンポスト状況を取得
        latest_data = recent_data.iloc[-1]
        compost_status = get_compost_status(
            latest_data["Temperature (°C)"],
            latest_data["Soil Moisture (%)"],
            latest_data["Gas Resistance (kΩ)"]
        )
    else:
        temperature = soil_moisture = gas_resistance = timestamps = []
        compost_status = "データがありません"

    # ログ出力で確認
    print(f"Temperature Data: {temperature}")
    print(f"Soil Moisture Data: {soil_moisture}")
    print(f"Gas Resistance Data: {gas_resistance}")
    print(f"Timestamps: {timestamps}")

    return render_template(
        "dashboard.html",
        temperature=temperature,
        soil_moisture=soil_moisture,
        gas_resistance=gas_resistance,
        timestamps=timestamps,
        compost_status=compost_status
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
