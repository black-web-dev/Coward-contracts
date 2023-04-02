import requests
import time

url = "https://api.opensea.io/asset/0x8E47863493EFF07afDB4d5CE9a5628BeD01865E8/"
# url = "https://testnets-api.opensea.io/api/v1/asset/0xFA1212eF6327564d5Fad7FFdf8ee2c57D087f930/"
update_flag = "/?force_update=true"

ids = [ i for i in range(1, 1001)]

for i in ids:
  req_url = url + str(i) + update_flag
  r = requests.get(req_url)
  print(i, r.status_code)
  time.sleep(0.3)
  