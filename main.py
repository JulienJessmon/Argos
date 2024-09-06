import ctypes
import time
import pyautogui
import pyperclip

# Load user32.dll which contains system-wide API functions
user32 = ctypes.windll.user32

class CURSORINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("flags", ctypes.c_ulong),
                ("hCursor", ctypes.c_void_p),
                ("ptScreenPos", ctypes.c_int * 2)]

# Function to get the current cursor shape
def get_cursor_shape():
    cursor_info = CURSORINFO()
    cursor_info.cbSize = ctypes.sizeof(CURSORINFO)
    if user32.GetCursorInfo(ctypes.byref(cursor_info)):
        # Check the cursor shape
        if cursor_info.hCursor == user32.LoadCursorW(0, 32649):  # 32649 is the IDC_HAND cursor
            pyautogui.keyDown('shift')
            pyautogui.keyUp('shift')
            print(pyperclip.paste())


# Call the function to check the cursor shape
while True:
    get_cursor_shape()
    time.sleep(5)