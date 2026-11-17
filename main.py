import os
import sys
import ctypes
import tkinter as tk
from PIL import Image, ImageTk


def res(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


mci = ctypes.windll.winmm.mciSendStringW


def mci_status(alias):
    buf = ctypes.create_unicode_buffer(64)
    mci(f"status {alias} mode", buf, 64, None)
    return buf.value


def start_scream():
    mci(f'open "{res("scream.mp3")}" type mpegvideo alias scream', None, 0, None)
    mci("play scream", None, 0, None)
    root.after(200, wait_scream)


def wait_scream():
    # когда крик закончился (один раз в начале) - запускаем музыку по кругу
    if mci_status("scream") == "playing":
        root.after(200, wait_scream)
        return
    mci("close scream", None, 0, None)
    mci(f'open "{res("music.mp3")}" type mpegvideo alias music', None, 0, None)
    mci("play music repeat", None, 0, None)


def close(_event=None):
    for alias in ("scream", "music"):
        mci(f"stop {alias}", None, 0, None)
        mci(f"close {alias}", None, 0, None)
    root.destroy()


root = tk.Tk()
root.configure(bg="black")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)
root.bind("<Escape>", close)          # Esc закрывает программу
root.protocol("WM_DELETE_WINDOW", close)

sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
img = Image.open(res("screen.png"))
scale = min(sw / img.width, sh / img.height)
img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
tk.Label(root, image=photo, bg="black").pack(expand=True)

start_scream()
root.mainloop()
