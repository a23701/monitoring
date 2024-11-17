import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# メール送信設定
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "compostmonitoring@gmail.com"  # 自分のメールアドレス
SENDER_PASSWORD = "abeLAB@2022"  # アプリパスワード
RECIPIENT_EMAIL = "a23701@g.ichinoseki.ac.jp"  # 送信先のメールアドレス

def send_alert(subject, message):
    """
    メールでアラートを送信
    Args:
        subject (str): メールの件名
        message (str): メールの本文
    """
    try:
        # メールの設定
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECIPIENT_EMAIL
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        # メール送信
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("アラートメールを送信しました！")

    except Exception as e:
        print(f"メール送信中にエラーが発生しました: {e}")
