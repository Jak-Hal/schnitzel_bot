#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import telegram
import datetime

# Set up Telegram bot new
bot = telegram.Bot(token='6252257467:AAED7Yl2bnmtN7dGq5qXnR9zli6T1by3MeM')
chat_id = '957054148'


# Define function to check if schnitzel is on the menu
def check_schnitzel():
    # Get today's date
    today = datetime.datetime.now().strftime('%A %d %B').capitalize()

    # Scrape the menu website
    url = 'https://www.teknikenshus.se/restaurang'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the menu items for today
    today_menu = soup.find('div', {'id': 'day-0'})

    # Check if schnitzel is on the menu
    schnitzel_found = False
    for item in today_menu.find_all('div', {'class': 'meal-description'}):
        if 'schnitzel' in item.text.lower():
            schnitzel_found = True
            break

    # Send a message to Telegram
    message = f'Schnitzel is{" " if schnitzel_found else " not "}on the menu today ({today}).'
    bot.send_message(chat_id=chat_id, text=message)

# Check for schnitzel at 5 PM on Sunday
if datetime.datetime.now().weekday() == 6 and datetime.datetime.now().hour == 17:
    check_schnitzel()
