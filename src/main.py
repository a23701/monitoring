import sys
import os

# srcディレクトリをモジュール検索パスに追加
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from sensors.gas_sensor import calculate_resistance
from sensors.temperature import read_temperature
from sensors.soil_moisture import read_adc, soil_moisture_percentage
from utils.logger import log_data
from utils.config import SOIL_MOISTURE_CHANNEL, MQ135_CHANNEL, LOG_FILE

def main():
    try:
        while True:
            # 温度センサー
            temperature = read_temperature()

            # 土壌水分センサー
            adc_value_soil = read_adc(SOIL_MOISTURE_CHANNEL)
            soil_moisture = soil_moisture_percentage(adc_value_soil)

            # MQ135ガスセンサー
            adc_value_gas = read_adc(MQ135_CHANNEL)
            gas_resistance = calculate_resistance(adc_value_gas)

            # データ表示
            print(f"Temperature: {temperature:.2f} °C, Soil Moisture: {soil_moisture:.2f} %, Gas Resistance: {gas_resistance:.2f} kΩ")

            # データ記録
            log_data(LOG_FILE, temperature, soil_moisture, gas_resistance)

    except KeyboardInterrupt:
        print("終了")

if __name__ == "__main__":
    main()
