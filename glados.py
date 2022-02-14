import requests
import json

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '26',
    'content-type': 'application/json;charset=UTF-8',
    'cookie': '_ga=GA1.2.2050194521.1639477580; koa:sess=eyJ1c2VySWQiOjExNzY5NCwiX2V4cGlyZSI6MTY2NTM5NzgyMDMwMSwiX21heEFnZSI6MjU5MjAwMDAwMDB9; koa:sess.sig=D_iTbGW7dJO3ToaVN9ndXbfOets; _gid=GA1.2.206998597.1644655233',
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
    "token":"glados_network"
}
data = json.dumps(data)
response = requests.post(url=url, headers=headers, data=data)
print(response)
# with open('res.txt', 'w') as res:
#     res.write(response.content.decode('utf-8'))

