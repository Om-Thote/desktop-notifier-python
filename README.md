Desktop Notifier Project

Project Overview:- The Desktop Notifier is a Python-based application that provides popup notifications on your computer screen at specified intervals. It's designed to help users remember important tasks, take breaks, or follow any other routine reminders. The application runs in the background and periodically sends notifications with a custom title and message, making it useful for improving productivity and time management.

Tech Stack:-
Language: Python
Libraries:plyer: Used to create cross-platform desktop notifications.
          time: Utilized to set intervals for repeating notifications.

Key Features:-
Custom Notifications: The user can define the title and message of each notification, making the app versatile for different use cases like reminders to drink water, take breaks, or check emails.
Time Interval Setting: Notifications can be set to appear at custom intervals (e.g., every 30 minutes, 1 hour, etc.).
Cross-Platform Support: Thanks to the plyer library, this app works across different operating systems, including Windows, macOS, and Linux.
Background Process: The notifier runs continuously in the background, freeing the user from needing to interact with it after starting.

How it works:-
The plyer module is used to create cross-platform notifications.
The user defines a title, message, and time interval.
The program runs a loop to display the notification at the set intervals.

How to Run:-
Install dependencies: pip install plyer
Run the script: python notifier.py
Customize title, message, and interval as needed.

Use Case:-
Reminders for regular breaks during work.
Notifications for tasks, meetings, or medication alerts.
