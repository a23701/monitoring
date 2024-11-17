from w1thermsensor import W1ThermSensor

# センサーを初期化
sensor = W1ThermSensor()

try:
    # 温度データを取得
    temperature = sensor.get_temperature()
    print(f"Temperature: {temperature:.2f}°C")
except Exception as e:
    print(f"Error reading sensor: {e}")
