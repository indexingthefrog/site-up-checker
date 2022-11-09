import requests

global b
def checkurl(url):
    session = requests.Session()
    try:
        b = session.get(url)
    except b.exceptions.ConectionError:
        return 'bad url'
    if b.status_code == 200: 
        return 'OK'
    else:
        return 'BAD'


print(checkurl('https://replit.com')) ## test
