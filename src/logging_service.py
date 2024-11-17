from sensors.temperature import read_temperature
from sensors.soil_moisture import read_adc, soil_moisture_percentage
from sensors.gas_sensor import calculate_resistance
from utils.logger import log_data  # CSVへの記録
from pathlib import Path
from datetime import datetime

# ファイルの保存場所
LOG_FILE_CSV = Path("/home/kon/monitoring/data/sensor_data.csv")
LOG_FILE_TEXT = Path("/home/kon/monitoring/logging.log")  # テキストログファイル

def log_to_text_file(file_path, timestamp, temperature, soil_moisture, gas_resistance):
    """
    テキストログファイルにデータを記録
    Args:
        file_path (Path): ログファイルのパス
        timestamp (str): 実行日時
        temperature (float): 温度
        soil_moisture (float): 土壌水分
        gas_resistance (float): ガス抵抗
    """
    with open(file_path, mode='a', newline='') as file:
        file.write(f"{timestamp}, 温度: {temperature}°C, 土壌水分: {soil_moisture}%, ガス抵抗: {gas_resistance}kΩ\n")

def main():
    try:
        # センサー値を取得
        temperature = read_temperature()
        adc_value_soil = read_adc(channel=0)
        soil_moisture = soil_moisture_percentage(adc_value_soil)
        adc_value_gas = read_adc(channel=1)
        gas_resistance = calculate_resistance(adc_value_gas)

        # 現在の日時
        timestamp = datetime.now().isoformat()

        # テキストログに記録
        log_to_text_file(LOG_FILE_TEXT, timestamp, temperature, soil_moisture, gas_resistance)

        # CSVファイルに記録
        log_data(LOG_FILE_CSV, temperature, soil_moisture, gas_resistance)

        print(f"データ記録成功: {timestamp}, 温度={temperature}°C, 土壌水分={soil_moisture}%, ガス抵抗={gas_resistance}kΩ")

    except Exception as e:
        print(f"データ取得中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
