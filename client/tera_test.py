import requests
from requests.packages import urllib3

urllib3.disable_warnings()

r = requests.get("https://194.1.237.94/api/v1/GetCurrentInfo", verify=False)
print(r.json())
