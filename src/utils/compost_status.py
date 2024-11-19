def get_compost_status(temperature, soil_moisture, gas_resistance):
    """
    コンポストの成熟度を判定する
    """
    if temperature < 30 and soil_moisture < 40 and gas_resistance < 0.5:
        return "成熟 (Ready)"
    elif 30 <= temperature <= 50:
        return "中期分解 (Mid Stage)"
    else:
        return "初期分解 (Early Stage)"
