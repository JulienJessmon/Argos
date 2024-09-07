import ctypes
import time
import pyautogui
import pyperclip
import re
import keyboard

# Load user32.dll which contains system-wide API functions
user32 = ctypes.windll.user32

# Define constants
IDC_HAND = 32649
SLEEP_TIME = 3


class CURSORINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("flags", ctypes.c_ulong),
                ("hCursor", ctypes.c_void_p),
                ("ptScreenPos", ctypes.c_int * 2)]

class LinkCC:

    def __init__(self):
        self.last_cursor_shape = None

    # Function to get the current cursor shape
    def get_cursor_shape(self) -> None:
        try:
            cursor_info = CURSORINFO()
            cursor_info.cbSize = ctypes.sizeof(CURSORINFO)
            if user32.GetCursorInfo(ctypes.byref(cursor_info)):
                # Check the cursor shape
                if cursor_info.hCursor == user32.LoadCursorW(0, IDC_HAND):
                    self.handle_hand_cursor()
                else:
                    self.last_cursor_shape = None
            else:
                print("Failed to get cursor info")
        except Exception as e:
            print(f"Error: {e}")

    # Handle hand cursor
    def handle_hand_cursor(self) -> None:
        try:
            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')
            link = pyperclip.paste()
            if self.is_domain(link):
                print(f"Valid link detected: {link}")
            else:
                print(f"Invalid link detected: {link}")
        except Exception as e:
            print(f"Error: {e}")

    # Check if link is valid
    @staticmethod
    def is_domain(string: str) -> bool:
        domain = r"^https?://([a-zA-Z0-9.]+)(?:/|$)"
        if string is None:
            return False
        if re.search(domain, string):
            return True
        else:
            return False

# Create an instance of the LinkCC class
link_cc = LinkCC()

# Call the function to check the cursor shape and exit prgm if spacebar is pressed
while True:
    link_cc.get_cursor_shape()
    time.sleep(SLEEP_TIME)
    if keyboard.is_pressed('ctrl'): # actin wierd hafta fix
        print("ctrl pressed. Exiting...")
        break