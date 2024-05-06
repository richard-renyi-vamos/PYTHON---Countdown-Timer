import tkinter as tk
from tkinter import messagebox
import time


class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        
        self.label = tk.Label(master, text="Set Timer (in seconds):")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.button = tk.Button(master, text="Start Timer", command=self.start_timer)
        self.button.pack()
        
        self.timer_label = tk.Label(master, text="")
        self.timer_label.pack()
        
        self.seconds_left = 0
        self.timer_running = False

    def start_timer(self):
        if self.timer_running:
            messagebox.showinfo("Warning", "Timer is already running!")
            return
        
        try:
            self.seconds_left = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            return
        
        if self.seconds_left <= 0:
            messagebox.showerror("Error", "Please enter a positive number!")
            return
        
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.seconds_left > 0:
            self.timer_label.config(text=f"Time left: {self.seconds_left} seconds")
            self.seconds_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.timer_running = False
            messagebox.showinfo("Info", "Time's up!")

def main():
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
