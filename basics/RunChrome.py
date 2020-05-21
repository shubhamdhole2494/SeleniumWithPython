import time

from selenium import webdriver
import os
import requests
import json

# class RunChrome():
#     def TestChrome(self):
#         driverLocation = "/Users/sdhole/Documents/python_workspace/SeleniumWithPython/libs/chromedriver"
#         os.environ["webdriver.chrome.driver"] = driverLocation
#         driver = webdriver.Chrome(driverLocation)
#         driver.get("https://www.youtube.com/")
#
# rc = RunChrome()
# rc.TestChrome()

url = 'https://qa-api.awseventservices.com/events/reinvent-20/users/'
header = {'x-api-key':'mwISZeE0fMvjX7aZUAZbVY97Zx5qamgUWRg9obI3'}

header1 = {
  'Content-Type' : 'application/json',
  'Accept' : 'ver=1.0',
  'x-api-key' : 'mwISZeE0fMvjX7aZUAZbVY97Zx5qamgUWRg9obI3',
  'Host' : 'qa-api.awseventservices.com',
  'User-Agent' :'PostmanRuntime/7.24.1',
  'Accept-Encoding' : 'gzip, deflate, br',
  'Connection' : 'keep-alive',
  'Content-Length' : '952',
  'Postman-Token' : '1b940cd2-6e03-4ef6-b439-0f674b691f67'

}

def post_token():
  username = 'htessmann'
  r = requests.post(url + 'token', json={
    "userName": username,
    "password": "mobTest123!"
  }, headers=header)
  return r.text

token_response = json.loads(str(post_token()))
print(token_response)
identityId = token_response['data']['tokenData']['identityId']
token = token_response['data']['tokenData']['token']


def post_credentilas():
  r = requests.post('https://qa-api.awseventservices.com/events/reinvent-20/credentials', json={
    "IdentityId": identityId,
    "Token": token
  }, headers=header)
  print(r.text)
#host = qa-cms-events.awseventservices.com
#port = 443

post_token()
time.sleep(5)
post_credentilas()

header2 = {
  'Accept' : 'ver=1.0',
  'x-api-key' : 'mwISZeE0fMvjX7aZUAZbVY97Zx5qamgUWRg9obI3',
  'Host' : 'qa-api.awseventservices.com',
  'X-Amz-Security-Token' : 'IQoJb3JpZ2luX2VjEKL//////////wEaCXVzLWVhc3QtMSJHMEUCIQDTpSdRAv5wjew8QXqlrLOORotYkR9QBDEmd4lHUrUBoAIgbH1WKKnkZnt2p+roKh13TCl0kysMCVvGVv7AwXY1ejYq4AMI2///////////ARACGgwxMDUwNjczNDA0MTAiDMct7EKUsn8Ac4yzySq0AwvOZ0PDiCYhyG6tD4hFJeIAqgPfSj+piPowqNXHjaoZbv5uounrQGQwUS8MDJgKpZIEiuqdeicqqjP8N4wLbDcLypZfutIVO1dfDYgImDMjiG0EeQCoqgWJUobSvvV+N66bjj8d7saQ6quNydgb7yxFvEIczEc69p891XsN/c9avQz3A0LCahMwxIqixTJEHn8XNvhU64DC7ttrONOPW/pL3jxQ5xxJa7IoIaEvcMoatArjkX2et61cTFGUmQ8z6TLNPNhVLNemgFMioV63bgckD476FoleBMJd98h0i5kFmF59jgcE5mkUQsCK7+otqS/bb266qI9bu7ne2Woe1uX9vys3Gi1W05MvR0x65PtmoaRas6hjtedo9EZ2suFYrQlvHc1KUSKhqIHHXRuQyw2coI/vBT2ptTzwtUrp0ziA+3IYeWIYlHGyZhraIwj8oP11JesAzMMfi7PY8Zb0/WCYj71Ea80ceToIe/GtEbx02xSUAoEuUMMQ6O6T3SNS908tj7bqfZk7EE7xLs7M+EwE4SHbsvruEyH/XYXVMWtYI4jh56US6IbuCGZrE6vO6ynTe30wt67W9QU6ywJkIBc1FLqq5mkVy2qj6xefW06BrLS0m2IpgY8R4sQrm06Enkz2GKLo1n/VJBsodx5HROayKuXAE77ecFXj0o9WY98QcoJJSDQ5OLEcGKVcq/Py6Msq7DL9Kdyd8ltRsWN0yq4RsGGNQbivfYgY39gaaqsyEUnkCi3MAgVFcb4KPqNlybmVrWq56D71VZjWnqnZ52VLaB4mxmCR04Ixal5lLmVryGMgyOeMe2YFPiG7vtdkr78c+idWBLhj7i1MG2ZPZ8MiaxJHayUiSnzvXhV8LxgbCdzDBogY7ZDC0x7Nf4PaOI2SllVIMwZxyfNjOkLbs8qGPG3fZspiDf1D4z0uEEvFSvlSYhTLnt4HL1wn+Ccc8mIkwOneWRFSlDMKMs/ta46Rx0yA+RFfNQjfzxXwYHJiYyNGH3u4P45EvqHEM9phRDPXLGDddN1R',
  'X-Amz-Date' : '20200508T182138Z',
  'Authorization' : 'AWS4-HMAC-SHA256 Credential=ASIARQ5UAMJ5MARF7QEU/20200508/us-east-1/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date;x-amz-security-token;x-api-key, Signature=d41095cd4bbaba5104bea2182ee25c267015df21149ab1e0f306af269ec451f8',
  'Accept-Encoding' : 'gzip, deflate, br',
  'Connection' : 'keep-alive'
}

r = requests.get('https://qa-api.awseventservices.com/events/reinvent-20/sessions/catalog',headers = header2)
print(r.text)