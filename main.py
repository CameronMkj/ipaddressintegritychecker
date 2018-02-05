import requests
import os

os.system('cls' if os.name == 'nt' else 'clear')
ipAddress = raw_input("What is the requested IP address you want to scan? ")
privateApiKey = "APIKEY"
#privateApiKey can be generated on account creation with 'ipqualityscore.com'.

r = requests.get("https://www.ipqualityscore.com/api/json/ip/" + privateApiKey + "/" + ipAddress)

os.system('cls' if os.name == 'nt' else 'clear')
print("-" * 80)
print("ISP = " + r.json()['ISP'])
print("Organization = " + r.json()['organization'])
print("City = " + r.json()['city'])
print("Country Code = " + r.json()['country_code'])
print("Region = " + r.json()['region'])
print("Proxy = " + str(r.json()['proxy']))
print("Tor = " + str(r.json()['tor']))
print("VPN = " + str(r.json()['vpn']))
print("Is Crawler = " + str(r.json()['is_crawler']))
print("Mobile = " + str(r.json()['mobile']))
print("Fraud Score = " + str(r.json()['fraud_score']))
print("Timezone = " + str(r.json()['timezone']))
print("-" * 80)