import grequests
import time

start_time = time.time()
# Create a 10000 requests
urls = ['http://127.0.1.1:9000/recipes']*10000
print(urls)
rs = (grequests.head(u) for u in urls)

# Send them.
grequests.map(rs)
print(time.time())
print(time.time() - start_time) # Result was: 9.66666889191