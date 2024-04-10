import tkinter as tk
import datetime
import time
import winsound
from threading import Thread

class AlarmClockApp:
    def __init__(self, master):
        self.master = master
        master.title("Alarm Clock")
        master.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
        tk.Label(self.master, text="Set Time", font=("Helvetica", 15, "bold")).pack()

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.create_option_menu("Hour", 24)
        self.create_option_menu("Minute", 60)
        self.create_option_menu("Second", 60)

        tk.Button(self.master, text="Set Alarm", font=("Helvetica", 15), command=self.set_alarm).pack(pady=20)

    def create_option_menu(self, label_text, max_value):
        var = tk.StringVar(self.master)
        values = tuple(f"{i:02d}" for i in range(max_value))
        var.set(values[0])

        option_menu = tk.OptionMenu(self.frame, var, *values)
        option_menu.pack(side=tk.LEFT)
        setattr(self, label_text.lower(), var)

    def set_alarm(self):
        t1 = Thread(target=self.alarm)
        t1.start()

    def alarm(self):
        while True:
            set_alarm_time = f"{self.hour.get()}:{self.minute.get()}:{self.second.get()}"
            time.sleep(1)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time, set_alarm_time)
            if current_time == set_alarm_time:
                print("Time to Wake up")
                winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

def main():
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
