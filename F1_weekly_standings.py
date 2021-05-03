# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import math
import os
from twilio.rest import Client

def print_start(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'started, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_start('f1 scrapper')
    page = requests.get("https://www.formula1.com/en/results.html/2021/drivers.html")
    #page = requests.get("https://tickets.formula1.com/en")
    print(page.status_code)
    if page.status_code != 200:
        print_start("closing scrapper")
        exit()
    soup = BeautifulSoup(page.content, 'html5lib')
    table = soup.find_all('tr')
    standings = []
    table = table[1:]
    for item in table:
        driver = []
        driver.append(item.contents[5].contents[1].contents[1].contents[0])
        driver.append(int(item.contents[11].contents[0]))
        standings.append(driver)

    #Your Account Sid and Auth Token from twilio.com/console
    #and set the environment variables. See http://twil.io/secure


    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=str(standings[0])+str(standings[1])+str(standings[2]),
        from_='+12404534901',
        to='+14084599761'
    )

    print(message.sid)






