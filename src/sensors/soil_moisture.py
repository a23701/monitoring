import spidev

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1350000

def read_adc(channel):
    """
    ADC値を読み取る関数
    Args:
        channel: ADCチャンネル (0〜7)
    Returns:
        ADC値 (0〜1023)
    """
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    value = ((adc[1] & 3) << 8) + adc[2]
    return value

def soil_moisture_percentage(adc_value, min_value=0, max_value=1023):
    """
    土壌水分をパーセンテージに変換する関数
    Args:
        adc_value: ADC値 (0〜1023)
    Returns:
        土壌水分 (%) (0〜100)
    """
    percentage = ((adc_value - min_value) / (max_value - min_value)) * 100
    inverted_percentage = 100 - percentage
    return max(0, min(inverted_percentage, 100))
