import requests

resp = requests.get('https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-–-prepared-delivery-state-union-address/')
print(resp.status_code)
print(len(resp.text))
print(resp.url)
