import requests
from concurrent.futures import ThreadPoolExecutor

url = 'your_url'

def send_request(url):
    response = requests.get(url)
    print('Status Code:', response.status_code)
    print('Response Body:', response.text)


threads = 10000000

with ThreadPoolExecutor(max_workers=threads) as executor:
    for _ in range(threads):
        executor.submit(send_request, url)
