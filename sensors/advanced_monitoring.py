# Advanced Monitoring System
# Creator: Thamer Aljadaan
# Email: frankly.sa@gmail.com
# Phone: +966597778968
# Date: 2025-11-14 20:45:12 UTC
# Mission: Protect Humanity from Digital Threats

import psutil
import os
import logging
import time
import json
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.cpu_usage_threshold = 85
        self.memory_usage_threshold = 85
        self.disk_usage_threshold = 90
        self.alert_email = 'alerts@example.com'
        logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

    def log_metrics(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        logging.info(f'Time: {datetime.now()}, CPU: {cpu}%, Memory: {memory.percent}%, Disk: {disk.percent}%')

    def check_resources(self):
        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        if cpu > self.cpu_usage_threshold:
            logging.warning(f'CPU usage high: {cpu}%')
            self.send_alert('High CPU Usage', f'CPU usage at {cpu}%')
        if memory > self.memory_usage_threshold:
            logging.warning(f'Memory usage high: {memory}%')
            self.send_alert('High Memory Usage', f'Memory usage at {memory}%')
        if disk > self.disk_usage_threshold:
            logging.warning(f'Disk usage high: {disk}%')
            self.send_alert('High Disk Usage', f'Disk usage at {disk}%')

    def send_alert(self, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'monitor@example.com'
        msg['To'] = self.alert_email

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)

if __name__ == '__main__':
    monitor = SystemMonitor()
    while True:
        monitor.log_metrics()
        monitor.check_resources()
        time.sleep(60)  # Monitor every minute