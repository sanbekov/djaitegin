import pyqrcode

s = "http://baskino.me/films/trillery/34588-vyshka.html/"
url = pyqrcode.create(s)

url.svg("Damon", scale=8)