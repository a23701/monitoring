import time
from mq135_utils import calibrate_r0, calculate_resistance

def read_adc(channel):
    """
    ADC値を読み取る関数（MCP3008を利用）
    Args:
        channel: ADCのチャンネル番号
    Returns:
        ADC値 (0〜1023)
    """
    import spidev
    spi = spidev.SpiDev()
    spi.open(0, 0)
    spi.max_speed_hz = 1350000

    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 3) << 8) + adc[2]
    spi.close()
    return value

def main():
    """
    キャリブレーションを行うメイン関数
    """
    print("キャリブレーションを開始します。クリーンな空気中で実施してください。")
    time.sleep(2)

    # ADCのチャンネル設定
    MQ135_CHANNEL = 1  # MQ135が接続されているチャンネル番号

    # ADC値を取得
    adc_value = read_adc(MQ135_CHANNEL)
    print(f"ADC Value: {adc_value}")

    # R0を計算
    try:
        r0 = calibrate_r0(adc_value)
        print(f"Calibrated R0: {r0:.2f} kΩ")

        # 保存する場合
        with open("calibration_data.txt", "w") as f:
            f.write(f"R0: {r0:.2f}\n")

        print("キャリブレーションが完了しました。R0の値はcalibration_data.txtに保存されました。")

    except ValueError as e:
        print(f"エラー: {e}")

if __name__ == "__main__":
    main()
