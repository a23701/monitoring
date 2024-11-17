import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def visualize_data(file_path):
    """
    CSVファイルのデータを可視化し、画像として保存する関数
    Args:
        file_path: データが保存されたCSVファイルのパス
    """
    try:
        # データの読み込み
        data = pd.read_csv(file_path)

        # データの確認
        if data.empty:
            print("データがありません。CSVファイルを確認してください。")
            return

        # タイムスタンプを日時型に変換
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data.set_index('Timestamp', inplace=True)

        # プロット
        plt.figure(figsize=(10, 8))
        data[['Temperature (°C)', 'Soil Moisture (%)', 'Gas Resistance (kΩ)']].plot(
            subplots=True, figsize=(10, 8), title="Sensor Data Over Time"
        )

        # 画像保存用ディレクトリを作成
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)

        # 画像として保存
        output_file = output_dir / "sensor_data_plot.png"
        plt.tight_layout()
        plt.savefig(output_file)
        print(f"グラフを '{output_file}' に保存しました。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")
