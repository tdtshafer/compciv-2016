import requests

resp1 = requests.get('https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress')
resp2 = requests.get('https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address')
resp3 = requests.get('https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-address')
resp4 = requests.get('https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address')
resp5 = requests.get('https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address')
resp6 = requests.get('https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015')
resp7 = requests.get('https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address')

array = [resp1, resp2, resp3, resp4, resp5, resp6, resp7]

for resp in array:
  print(resp.url)
  print(len(resp.text))
  print(resp.text.count('Applause'))

  


    
    
    
    
