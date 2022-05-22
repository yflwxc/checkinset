import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '26',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': '_ga=GA1.2.1504803283.1653209821; _gid=GA1.2.1931333058.1653209821; koa:sess=eyJ1c2VySWQiOjE2MjQ4NCwiX2V4cGlyZSI6MTY3OTEzNDIxNjYzNCwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=cUEQZ5TpaQrBcAryT2vrR3enL1o; __stripe_mid=3d5e7b7e-b163-452a-bb9c-e27d59b32a8ccf5bb7; __stripe_sid=707afb32-127a-4f3f-85aa-e5280fa849921e1f4b',
    'origin': 'https://glados.rocks',
    'referer': 'https://glados.rocks/console/checkin',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
}

url = 'https://glados.rocks/api/user/checkin'
data = {
    "token":"glados.network"
}
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response.text)
