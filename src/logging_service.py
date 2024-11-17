from utils.logger import log_data
from sensors.temperature import read_temperature
from sensors.soil_moisture import read_adc, soil_moisture_percentage
from sensors.gas_sensor import calculate_resistance
from pathlib import Path

# CSVファイルの保存場所
LOG_FILE = Path("/home/kon/monitoring/data/sensor_data.csv")

def main():
    try:
        # センサー値を取得
        temperature = read_temperature()
        adc_value_soil = read_adc(channel=0)  # 土壌水分センサーのADC値を取得
        soil_moisture = soil_moisture_percentage(adc_value_soil)  # 土壌水分を計算
        adc_value_gas = read_adc(channel=1)  # ガスセンサーのADC値を取得
        gas_resistance = calculate_resistance(adc_value_gas)  # ガス抵抗を計算

        # ロギング
        log_data(LOG_FILE, temperature, soil_moisture, gas_resistance)
        print(f"データ記録成功: 温度={temperature}°C, 土壌水分={soil_moisture}%, ガス抵抗={gas_resistance}kΩ")

    except Exception as e:
        print(f"データ取得中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
