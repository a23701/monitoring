import spidev
import time

# SPI設定
spi = spidev.SpiDev()
spi.open(0, 0)  # SPIデバイス0, チップセレクト0
spi.max_speed_hz = 1350000

# ADC値を読み取る関数
def read_channel(channel):
    # 3バイトのデータを送信して、センサーの値を取得
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# ADC値を0〜100%のパーセンテージに変換する関数
def convert_to_percentage(adc_value, min_value=0, max_value=1023):
    percentage = ((adc_value - min_value) / (max_value - min_value)) * 100
    return max(0, min(percentage, 100))  # 範囲外を制限

try:
    while True:
        # CH0から土壌水分のADC値を取得
        soil_moisture_adc = read_channel(0)

        # パーセンテージに変換
        soil_moisture_percentage = convert_to_percentage(soil_moisture_adc)

        # 結果を出力
        print(f"Soil Moisture Level: {soil_moisture_percentage:.2f}%")

        # 1秒ごとに更新
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
    print("終了")

