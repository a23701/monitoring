import spidev
import time

# SPI設定
spi = spidev.SpiDev()
spi.open(0, 0)  # SPIデバイス0, チップセレクト0
spi.max_speed_hz = 1350000

# ADCチャンネルから値を読み取る関数
def read_channel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# パーセンテージに変換する関数
def convert_to_percentage(adc_value, min_value=0, max_value=1023):
    percentage = ((adc_value - min_value) / (max_value - min_value)) * 100
    return max(0, min(percentage, 100))  # 0〜100%の範囲内に制限

try:
    while True:
        # 土壌水分センサー（CH0）のデータ取得
        soil_moisture_adc = read_channel(0)
        soil_moisture_percentage = convert_to_percentage(soil_moisture_adc)
        print(f"Soil Moisture Level: {soil_moisture_percentage:.2f}%")

        # MQ135センサー（CH1）のデータ取得
        mq135_adc = read_channel(1)
        gas_level_percentage = convert_to_percentage(mq135_adc)
        print(f"MQ135 Gas Level: {gas_level_percentage:.2f}%")

        # 1秒間隔で更新
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
    print("終了")
