import urllib
response = urllib.request.urlopen("http://python.org/")
print (response.headers)
'''Date: Fri, 30 Mar 2012 09:24:55 GMT
Server: Apache/2.2.16 (Debian)
Last-Modified: Fri, 30 Mar 2012 08:42:25 GMT
ETag: "105800d-4b7b-4bc71d1db9e40"
Accept-Ranges: bytes
Content-Length: 19323
Connection: close
Content-Type: text/html
X-Pad: avoid browser bug
'''
print(response.header['Content-Type'])

'text/html'
print(content = request.read())
