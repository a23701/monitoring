from mq135_utils import calculate_resistance, calibrate_r0

# サンプルADC値（テスト用）
sample_adc_value = 512  # 仮のADC値（実測値に置き換え）

# キャリブレーションのテスト
print("Testing MQ135 Calibration...")
r0 = calibrate_r0(sample_adc_value)
print(f"R0: {r0:.2f} kΩ")

# 抵抗値計算のテスト
rs = calculate_resistance(sample_adc_value)
print(f"Rs: {rs:.2f} kΩ")
