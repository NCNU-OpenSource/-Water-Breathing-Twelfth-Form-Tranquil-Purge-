import os
import time
from datetime import datetime, timezone
import RPi.GPIO as GPIO

# 設置 GPIO 模式
GPIO.setmode(GPIO.BCM)
LED_PIN = 17  # 假設你將 LED 接在 GPIO 17
GPIO.setup(LED_PIN, GPIO.OUT)

# 初始化 LED 狀態
GPIO.output(LED_PIN, GPIO.LOW)

def clear_old_logs():
    """
    清除舊的日誌文件。
    """
    try:
        os.system("sudo truncate -s 0 /var/log/syslog")
        print("日誌文件已清除。")
    except Exception as e:
        print(f"清除日誌時發生錯誤: {e}")

def trigger_led():
    """
    控制 LED 亮 5 秒。
    """
    print("LED 開啟，等待 5 秒...")
    GPIO.output(LED_PIN, GPIO.HIGH)  # 開啟 LED
    time.sleep(2)                   # 等待 2 秒
    GPIO.output(LED_PIN, GPIO.LOW)  # 關閉 LED
    print("LED 已關閉。")

def stop_ping():
    """
    停止所有正在執行的 ping 程序。
    """
    try:
        os.system("sudo pkill -f ping")  # 終止包含 "ping" 的進程
        print("所有 ping 程序已停止。")
    except Exception as e:
        print(f"停止 ping 時發生錯誤: {e}")

def monitor_logs():
    """
    監控日誌文件，檢查是否有目標封包的日誌記錄。
    """
    try:
        with open('/var/log/syslog', 'r') as log_file:
            for line in log_file:
                if "Yellow Blocked" in line:
                    print(f"偵測到目標封包日誌: {line.strip()}")
                    # 偵測到後執行停止ping、清除日誌、亮燈
                    stop_ping()    # 停止 ping 程序
                    clear_old_logs()  # 清除日誌
                    trigger_led()  # 亮燈
                    return True  # 偵測到後返回 True
    except FileNotFoundError:
        print("未找到日誌文件，請確認路徑。")
    except Exception as e:
        print(f"監控日誌時發生錯誤: {e}")
    return False  # 未偵測到則返回 False

def main():
    try:
        print("開始監控日誌...")
        while True:
            if monitor_logs():  # 如果偵測到目標日誌
                pass  # 偵測到後繼續監控，並處理停止ping、亮燈、清除日誌
            time.sleep(1)  # 每秒檢查一次
    except KeyboardInterrupt:
        print("程式中斷，清理 GPIO...")
    finally:
        GPIO.cleanup()  # 清理 GPIO 資源
        print("GPIO 已清理，程式結束。")

if __name__ == "__main__":
    main()
