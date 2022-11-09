import requests
import time
from colorama import Fore

def checkurl(url):
    session = requests.Session()
    try:
        b = session.get(url)
    except Exception:
        return 'bad url'
    if b.status_code == 200: 
        return 'OK'
    else:
        return 'BAD'

## checks every minuite
def auto_update(url): 
    while True:
        time.sleep(60)
        if checkurl(url) == 'OK': 
            print(Fore.GREEN + 'WEBSITE IS UP!')
        else: 
            print(Fore.RED + 'WEBSITE IS DOWN :/')

auto_update('https://replit.com') ## example website
