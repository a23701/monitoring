from sensors.temperature import read_temperature
from sensors.soil_moisture import read_adc, soil_moisture_percentage
from sensors.gas_sensor import calculate_resistance
from utils.logger import log_data  # CSVへの記録
from pathlib import Path
from datetime import datetime  # ← これが必要
import RPi.GPIO as GPIO
import dht11
import time

# GPIOの初期化
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)
DHT11_PIN = 18
dht11_instance = dht11.DHT11(pin=DHT11_PIN)

# ファイルの保存場所
LOG_FILE_CSV = Path("/home/kon/monitoring/data/sensor_data.csv")
LOG_FILE_TEXT = Path("/home/kon/monitoring/logging.log")  # テキストログファイル

def log_to_text_file(file_path, timestamp, temperature, soil_moisture, gas_resistance, dht_temp, dht_humidity):
    """
    テキストログファイルにデータを記録
    """
    with open(file_path, mode='a', newline='') as file:
        file.write(f"{timestamp}, 温度: {temperature}°C, 土壌水分: {soil_moisture}%, ガス抵抗: {gas_resistance}kΩ, "
                   f"DHT温度: {dht_temp}°C, 湿度: {dht_humidity}%\n")

def read_dht11():
    """
    DHT11センサーから温度と湿度を取得
    """
    for _ in range(3):  # 最大3回リトライ
        result = dht11_instance.read()
        if result.is_valid():
            return result.temperature, result.humidity
        time.sleep(2)  # リトライ間隔
    return None, None  # 失敗時

def main():
    try:
        # センサー値を取得
        temperature = read_temperature()
        adc_value_soil = read_adc(channel=0)
        soil_moisture = soil_moisture_percentage(adc_value_soil)
        adc_value_gas = read_adc(channel=1)
        gas_resistance = calculate_resistance(adc_value_gas)

        # DHT11から温度と湿度を取得
        dht_temp, dht_humidity = read_dht11()
        if dht_temp is None or dht_humidity is None:
            print("DHT11のデータ取得に失敗しました")
            dht_temp, dht_humidity = "N/A", "N/A"

        # 現在の日時
        timestamp = datetime.now().isoformat()

        # テキストログに記録
        log_to_text_file(LOG_FILE_TEXT, timestamp, temperature, soil_moisture, gas_resistance, dht_temp, dht_humidity)

        # CSVファイルに記録
        log_data(LOG_FILE_CSV, temperature, soil_moisture, gas_resistance, dht_temp, dht_humidity)

        print(f"データ記録成功: {timestamp}, 温度={temperature}°C, 土壌水分={soil_moisture}%, ガス抵抗={gas_resistance}kΩ, "
              f"DHT温度={dht_temp}°C, 湿度={dht_humidity}%")

    except Exception as e:
        print(f"データ取得中にエラーが発生しました: {e}")

if __name__ == "__main__":
    main()
