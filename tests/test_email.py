from alert_notifier import send_alert_email

# テスト用のメールアドレスと内容を設定
recipient_email = "a23701@g.ichinoseki.ac.jp"  # 受信者メールアドレス
subject = "テストアラート"
message = "これはテストメールです。"

# メール送信テスト
try:
    send_alert_email(recipient_email, subject, message)
except Exception as e:
    print(f"メール送信テスト中にエラーが発生しました: {e}")
