import requests

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
    
checkurl('https://replit.com') ## example website
