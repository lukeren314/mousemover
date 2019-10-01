from pynput import keyboard, mouse
import random
import time
import tkinter as tk

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

failsafe = True
on = True


def on_press(key):
    try:
        if(key.char == "`"):
            on = not on
    except AttributeError:
        print("unknown key")


def on_release(key):
    if key == keyboard.Key.esc:
        failsafe = False
        return(False)


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

while failsafe:
    if(on):
        mouse.Controller.move(random.randrange(0, width),
                              random.randrange(0, height))
        time.sleep(1)


# pip install pynput
# pip install pyinstaller
# pyinstaller --noconsole script.py
