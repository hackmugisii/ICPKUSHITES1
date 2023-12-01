


import tkinter as tk
from threading import Thread
import secrets
import time

class KeyRotator:
    def __init__(self, key_length=32, rotation_interval=5):
        self.key_length = key_length
        self.rotation_interval = rotation_interval
        self.current_key = self.generate_random_key()
        self.rotation_schedule = []  
        self.is_running = False

    def generate_random_key(self):
        num_bytes = self.key_length // 2
        random_bytes = secrets.token_bytes(num_bytes)
        random_key = secrets.token_hex(num_bytes)
        return random_key

    def rotate_key(self):
        new_key = self.generate_random_key()
        self.current_key = new_key
        return new_key

    def start_rotation(self):
        self.is_running = True
        while self.is_running:
            time.sleep(self.rotation_interval)
            self.rotate_key()

class KeyRotatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Key Rotator")

        self.key_rotator = KeyRotator()

        self.label = tk.Label(master, text="Current Key:")
        self.label.pack()

        self.key_var = tk.StringVar()
        self.key_var.set(self.key_rotator.current_key)
        self.key_label = tk.Label(master, textvariable=self.key_var, font=("Helvetica", 12), wraplength=400)
        self.key_label.pack()

        self.start_button = tk.Button(master, text="Start Rotation", command=self.start_rotation)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Rotation", command=self.stop_rotation)
        self.stop_button.pack()


#the display looked awful but ill edit till it's better
    def update_key(self):
        while self.key_rotator.is_running:
            self.key_var.set(self.key_rotator.current_key)
            time.sleep(1)

    def start_rotation(self):
        self.key_rotator_thread = Thread(target=self.key_rotator.start_rotation)
        self.key_rotator_thread.start()
        self.update_key_thread = Thread(target=self.update_key)
        self.update_key_thread.start()

    def stop_rotation(self):
        self.key_rotator.is_running = False
        self.key_rotator_thread.join()
        self.update_key_thread.join()

if __name__ == "__main__":
    root = tk.Tk()
    gui = KeyRotatorGUI(root)
    root.mainloop()


#ohhh yes!!!!