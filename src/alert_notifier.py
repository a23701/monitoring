import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.thresholds import ALERT_THRESHOLDS
import os

ALERT_EMAIL_FILE = "/home/kon/monitoring/data/alert_emails.txt"

def send_alert_email(to_email, subject, message):
    """
    アラートメールを送信する関数
    """
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "compostmonitoring@gmail.com"  # 自分のメールアドレス
    password = "btfzjuybtsmmvkxk"  # アプリパスワード

    try:
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
        server.quit()

        print(f"アラートメールが {to_email} に送信されました。")
    except Exception as e:
        print(f"メール送信中にエラーが発生しました: {e}")

def send_alert_to_all(subject, message):
    """
    登録されたすべてのメールアドレスにアラートを送信
    """
    if not os.path.exists(ALERT_EMAIL_FILE):
        print("メールアドレスリストが存在しません。")
        return

    with open(ALERT_EMAIL_FILE, "r") as file:
        emails = [line.strip() for line in file.readlines()]

    for email in emails:
        send_alert_email(email, subject, message)

def check_alert_conditions(temperature, soil_moisture, gas_resistance):
    """
    センサー値が閾値を超えている場合、アラートメッセージを生成する
    """
    alerts = []
    if temperature > ALERT_THRESHOLDS["temperature"]:
        alerts.append(f"温度が高すぎます: {temperature}°C")
    if soil_moisture < ALERT_THRESHOLDS["soil_moisture"]:
        alerts.append(f"土壌水分が低すぎます: {soil_moisture}%")
    if gas_resistance < ALERT_THRESHOLDS["gas_resistance"]:
        alerts.append(f"ガス濃度が高すぎます: {gas_resistance}kΩ")
    return alerts
