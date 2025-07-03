import psutil
import time
from plyer import notification

while True:
    battery = psutil.sensors_battery()
    if battery.percent >= 95:
        notification.notify(
            title="Battery Alert",
            message="Battery is at {}%. Please unplug the charger.".format(battery.percent),
            timeout=10
        )
    time.sleep(300)  # Check every 5 minutes
