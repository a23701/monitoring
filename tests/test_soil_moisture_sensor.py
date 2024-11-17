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

def convert_to_percentage(adc_value, min_value=0, max_value=1023):
    """
    ADC値を湿度のパーセンテージに変換する関数。
    湿っている状態で100%、乾いている状態で0%となるよう反転。
    Args:
        adc_value: ADCから取得した値 (0〜1023)
        min_value: ADC値の最小値（例: 0）
        max_value: ADC値の最大値（例: 1023）
    Returns:
        湿度のパーセンテージ (0〜100%)
    """
    # 通常のスケーリング
    percentage = ((adc_value - min_value) / (max_value - min_value)) * 100
    # 反転処理
    inverted_percentage = 100 - percentage
    return max(0, min(inverted_percentage, 100))  # 範囲を0〜100%に制限

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
