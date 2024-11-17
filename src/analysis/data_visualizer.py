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
        if data.empty or len(data) < 2:
            print("データが不足しています。少なくとも2件以上のデータが必要です。")
            return

        print("CSVデータを正常に読み込みました:")
        print(data.head())  # CSVの先頭データを表示

        # タイムスタンプを日時型に変換
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data.set_index('Timestamp', inplace=True)

        # プロット
        plt.figure(figsize=(10, 8))
        # グラフの修正版
        data[['Temperature (°C)', 'Soil Moisture (%)', 'Gas Resistance (kΩ)']].plot(
            subplots=True,
            figsize=(10, 8),
            title="Sensor Data Over Time",
            xlabel="Timestamp",
            ylabel="Values"
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

if __name__ == "__main__":
    # ファイルパスを指定
    csv_file_path = Path("data/sensor_data.csv")
    if not csv_file_path.exists():
        print(f"CSVファイルが見つかりません: {csv_file_path}")
    else:
        visualize_data(csv_file_path)
