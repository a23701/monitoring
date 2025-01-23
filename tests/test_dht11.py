import RPi.GPIO as GPIO
import dht11
import time
import datetime

# GPIOの初期化
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)  # GPIOのピン番号モードをBCMに設定

# DHT11センサーをGPIO18に接続
DHT11_PIN = 18
instance = dht11.DHT11(pin=DHT11_PIN)

try:
    while True:
        # DHT11センサーからデータを読み取る
        result = instance.read()
        if result.is_valid():
            # 現在時刻と温度・湿度を出力
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: %-3.1f°C" % result.temperature)
            print("Humidity: %-3.1f%%" % result.humidity)
        else:
            # 読み取りエラーが発生した場合のメッセージ
            print("Failed to get valid reading. Retrying...")

        # 次の読み取りまで6秒待機
        time.sleep(2)

except KeyboardInterrupt:
    # プログラム終了時にGPIOをクリーンアップ
    print("Cleanup")
    GPIO.cleanup()
