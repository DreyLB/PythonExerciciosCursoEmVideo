import urllib.request
try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('O site não está acessível')
else:
    print('Consegui acessar o site')
    print(site.read())
