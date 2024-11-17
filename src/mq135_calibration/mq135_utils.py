def calculate_resistance(adc_value, vcc=5.0, rl=10000):
    """
    ADC値からセンサー抵抗値Rsを計算する関数
    Args:
        adc_value: ADCから取得した値 (0〜1023)
        vcc: 電源電圧（デフォルト: 5.0V）
        rl: 負荷抵抗（デフォルト: 10kΩ）
    Returns:
        Rs: センサー抵抗値
    """
    vout = (adc_value / 1023.0) * vcc
    rs = ((vcc - vout) / vout) * rl
    return rs

def calibrate_r0(adc_value, clean_air_factor=3.6):
    """
    Rsから基準値R0を計算する関数
    Args:
        adc_value: ADCから取得した値 (0〜1023)
        clean_air_factor: クリーン空気中のRs/R0比
    Returns:
        R0: 基準抵抗値
    """
    rs = calculate_resistance(adc_value)
    r0 = rs / clean_air_factor
    return r0
