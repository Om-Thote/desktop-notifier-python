from plyer import notification
import time

# 1. Function to trigger notifications
def send_notification(title, message):
    try:
        # Trigger desktop notification
        notification.notify(
            title=title,  # Notification title
            message=message,  # Notification message
            timeout=10  # Duration the notification stays on the screen
        )
    except Exception as e:
        print(f"Error sending notification: {e}")

# 2. Main logic to send notifications periodically
if __name__ == "__main__":
    while True:
        # 3. Trigger notification every hour (or customizable)
        send_notification("Reminder", "Time to take a break!")
        
        # 4. Wait for 1 hour (3600 seconds) before next notification
        time.sleep(3600)  # Sleep for 3600 seconds
