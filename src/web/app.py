from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# センサーデータのパス
DATA_FILE = "/home/kon/monitoring/data/sensor_data.csv"

@app.route("/")
def dashboard():
    """
    ダッシュボード画面
    """
    # データ読み込み
    if os.path.exists(DATA_FILE):
        data = pd.read_csv(DATA_FILE)
        recent_data = data.tail(10)  # 最新の10件を取得
        temperature = recent_data["Temperature (°C)"].tolist()
        soil_moisture = recent_data["Soil Moisture (%)"].tolist()
        gas_resistance = recent_data["Gas Resistance (kΩ)"].tolist()
        timestamps = recent_data["Timestamp"].tolist()
    else:
        # データファイルが存在しない場合
        temperature = soil_moisture = gas_resistance = timestamps = []

    return render_template(
        "dashboard.html",
        temperature=temperature,
        soil_moisture=soil_moisture,
        gas_resistance=gas_resistance,
        timestamps=timestamps,
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
