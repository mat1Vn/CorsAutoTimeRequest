import requests
from bs4 import BeautifulSoup


cors_demo = 'http://cors-anywhere.herokuapp.com/corsdemo'
cors_acess = 'http://cors-anywhere.herokuapp.com/corsdemo?accessRequest='

req = requests.get(cors_demo)
soup = BeautifulSoup(req.text, 'html.parser')
acess_code = soup.find('input', {'name':'accessRequest'})['value']

header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Host':'cors-anywhere.herokuapp.com',
    'Referer': 'http://cors-anywhere.herokuapp.com/corsdemo',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:91.0) Gecko/20100101 Firefox/91.0'
}

print(cors_acess+acess_code)
req2 = requests.get(cors_acess+acess_code, headers=header)
print(req2)