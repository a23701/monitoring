import sys
import os
from pathlib import Path

# srcディレクトリをモジュール検索パスに追加
current_dir = Path(__file__).resolve().parent
src_dir = current_dir.parent / "src"
sys.path.insert(0, str(src_dir))

from utils.logger import log_data  # utils.loggerのインポート

# テスト用CSVファイル
TEST_LOG_FILE = Path("data/test_sensor_data.csv")

def test_logging():
    """
    ロギング関数の動作をテストする
    """
    try:
        # ダミーデータを記録
        log_data(TEST_LOG_FILE, temperature=25.5, soil_moisture=50.2, gas_resistance=1.8)

        # ログファイルの内容を確認
        if not TEST_LOG_FILE.exists():
            print("ログファイルが作成されていません。")
            return

        with open(TEST_LOG_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) < 2:  # ヘッダー行 + データ行
                print(f"データが記録されていません。行数: {len(lines)}")
            else:
                print("ロギング成功！記録されたデータ:")
                for line in lines:
                    print(line.strip())

    except Exception as e:
        print(f"ロギングのテスト中にエラーが発生しました: {e}")

if __name__ == "__main__":
    test_logging()
