import dht11
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
DHT11_PIN = 18  # DHT11のデータピンに接続したGPIOピン

def read_dht11():
    """
    DHT11センサーから温度と湿度を取得
    Returns:
        tuple: 温度 (float), 湿度 (float)
    """
    instance = dht11.DHT11(pin=DHT11_PIN)
    result = instance.read()

    if result.is_valid():
        return result.temperature, result.humidity
    else:
        print(f"Error: {result.error_code}")  # エラーコードを出力
        raise ValueError("DHT11センサーの読み取りに失敗しました")

if __name__ == "__main__":
    try:
        while True:
            temperature, humidity = read_dht11()
            print(f"温度: {temperature}°C, 湿度: {humidity}%")
            sleep(2)
    except KeyboardInterrupt:
        print("プログラムを終了します")
        GPIO.cleanup()
