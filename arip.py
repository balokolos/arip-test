"""Restart a systemd service every day at local midnight.

Set SERVICE to the service you want to restart, then run this script with
permissions to run ``systemctl restart`` (for example, via a systemd unit).
"""

from datetime import datetime, time, timedelta
import subprocess
import time as sleep

SERVICE = "your-service.service"

while True:
	now = datetime.now()
	tomorrow = now.date() + timedelta(days=1)
	midnight = datetime.combine(tomorrow, time.min)
	sleep.sleep((midnight - now).total_seconds())
	subprocess.run(["systemctl", "restart", SERVICE], check=True)
