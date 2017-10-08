import urllib
from urllib.request import urlopen
url = 'http://vivekshah.me/Portfolio/';
try:
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    head = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url,headers = head)
    res = urllib.request.urlopen(req)
    print(res.read().decode('utf-8'))
except Exception as e:
    print(str(e))
