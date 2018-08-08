import requests

url = 'http://127.0.1.1:9000/recipes/{}'

r = 10000

for i in range(r):
    res = requests.get(url.format(i))
    delay = res.headers.get("DELAY")
    d = res.headers.get("DATE")
    print("{}:{} delay {}".format(d, res.url, delay))