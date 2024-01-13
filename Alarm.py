import tkinter as tk
from tkinter import messagebox
import datetime
import time
import pygame

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Alarm Clock")

        self.label_time = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
        self.label_time.pack(pady=5)

        self.entry_time = tk.Entry(root)
        self.entry_time.pack(pady=5)

        self.label_message = tk.Label(root, text="Enter alarm message:")
        self.label_message.pack(pady=5)

        self.entry_message = tk.Entry(root)
        self.entry_message.pack(pady=5)

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.on_set_alarm)
        self.set_alarm_button.pack(pady=10)

        pygame.mixer.init()
        self.alarm_sound = pygame.mixer.Sound("C:\\Users\\alhus\\Downloads\\Iphone Alarm Sound Effect [TubeRipper.com].mp3")

    def read_alarm_time(self):
        try:
            with open("alarm_time.txt", "r") as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def write_alarm_time(self, alarm_time):
        with open("alarm_time.txt", "w") as file:
            file.write(alarm_time)

    def set_alarm(self, alarm_time, alarm_message):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                self.alarm_sound.play()
                messagebox.showinfo("Custom Alarm", alarm_message)
                break
            time.sleep(1)

    def on_set_alarm(self):
        alarm_time = self.entry_time.get()
        alarm_message = self.entry_message.get()
        self.write_alarm_time(alarm_time)

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
