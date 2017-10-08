import urllib.request

x = urllib.request.urlopen("https://vivekshah.me/Portfolio")
print(x.read())
