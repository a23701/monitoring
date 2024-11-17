def calculate_resistance(adc_value, vcc=5.0, rl=10000):
    """
    ADC値からセンサー抵抗値Rsを計算する関数
    Args:
        adc_value: ADCから取得した値 (0〜1023)
    Returns:
        Rs (kΩ)
    """
    if adc_value == 0:
        return float('inf')  # 無限大を返す
    vout = (adc_value / 1023.0) * vcc
    rs = ((vcc - vout) / vout) * rl
    return rs
