from w1thermsensor import W1ThermSensor

def read_temperature():
    """
    温度センサーから温度を取得する関数
    Returns:
        温度 (°C)
    """
    sensor = W1ThermSensor()
    return sensor.get_temperature()
