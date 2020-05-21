# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
# ABOUT THIS PYTHON SAMPLE: This sample is part of the AWS General Reference
# Signing AWS API Requests top available at
# https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html
#

# AWS Version 4 signing example

# EC2 API (DescribeRegions)

# See: http://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html
# This version makes a GET request and passes the signature
# in the Authorization header.
import json
import sys, os, base64, datetime, hashlib, hmac
import time

import requests  # pip install requests

# Code start
url = 'https://qa-api.awseventservices.com/events/reinvent-20/users/'
header = {'x-api-key':'mwISZeE0fMvjX7aZUAZbVY97Zx5qamgUWRg9obI3'}
print(header['x-api-key'])
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
  return r.text

credentials_response = json.loads(str(post_credentilas()))
accessKeyId = credentials_response['data']['stsTokenData']['accessKeyId']
secretAccessKey = credentials_response['data']['stsTokenData']['secretAccessKey']
sessionToken = credentials_response['data']['stsTokenData']['sessionToken']

#host = qa-cms-events.awseventservices.com
#port = 443

#post_token()
time.sleep(5)
#post_credentilas()

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
# def get_catalog():
#     r = requests.get('https://qa-api.awseventservices.com/events/reinvent-20/sessions/catalog', headers=header2)
#     print(r.text)


# Code ends
# ************* REQUEST VALUES *************
method = 'GET'
service = 'execute-api'
host = 'qa-api.awseventservices.com'
region = 'us-east-1'
endpoint = 'https://qa-api.awseventservices.com/events/reinvent-20/sessions/catalog'
request_parameters = ''


# Key derivation functions. See:
# http://docs.aws.amazon.com/general/latest/gr/signature-v4-examples.html#signature-v4-examples-python
def sign(key, msg):
    return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()


def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(('AWS4' + key).encode('utf-8'), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, 'aws4_request')
    return kSigning


# Read AWS access key from env. variables or configuration file. Best practice is NOT
# to embed credentials in code.
access_key = accessKeyId
secret_key = secretAccessKey
if access_key is None or secret_key is None:
    print('No access key is available.')
    sys.exit()

# Create a date for headers and the credential string
t = datetime.datetime.utcnow()
amzdate = t.strftime('%Y%m%dT%H%M%SZ')
datestamp = t.strftime('%Y%m%d')  # Date w/o time, used in credential scope

# ************* TASK 1: CREATE A CANONICAL REQUEST *************
# http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html

# Step 1 is to define the verb (GET, POST, etc.)--already done.

# Step 2: Create canonical URI--the part of the URI from domain to query
# string (use '/' if no path)
canonical_uri = '/'

# Step 3: Create the canonical query string. In this example (a GET request),
# request parameters are in the query string. Query string values must
# be URL-encoded (space=%20). The parameters must be sorted by name.
# For this example, the query string is pre-formatted in the request_parameters variable.
canonical_querystring = request_parameters

# Step 4: Create the canonical headers and signed headers. Header names
# must be trimmed and lowercase, and sorted in code point order from
# low to high. Note that there is a trailing \n.
canonical_headers = 'host:' + host + '\n' + 'x-amz-date:' + amzdate + '\n' + 'accept:' + 'application/json' + '\n' + 'x-amz-security-token:' + sessionToken + '\n' + 'x-api-key:' + header['x-api-key']

# Step 5: Create the list of signed headers. This lists the headers
# in the canonical_headers list, delimited with ";" and in alpha order.
# Note: The request can include any headers; canonical_headers and
# signed_headers lists those that you want to be included in the
# hash of the request. "Host" and "x-amz-date" are always required.
signed_headers = 'accept;host;x-amz-date;x-amz-security-token;x-api-key'

# Step 6: Create payload hash (hash of the request body content). For GET
# requests, the payload is an empty string ("").
payload_hash = hashlib.sha256(('').encode('utf-8')).hexdigest()

# Step 7: Combine elements to create canonical request
canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

# ************* TASK 2: CREATE THE STRING TO SIGN*************
# Match the algorithm to the hashing algorithm you use, either SHA-1 or
# SHA-256 (recommended)
algorithm = 'AWS4-HMAC-SHA256'
credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
string_to_sign = algorithm + '\n' + amzdate + '\n' + credential_scope + '\n' + hashlib.sha256(
    canonical_request.encode('utf-8')).hexdigest()

# ************* TASK 3: CALCULATE THE SIGNATURE *************
# Create the signing key using the function defined above.
signing_key = getSignatureKey(secret_key, datestamp, region, service)

# Sign the string_to_sign using the signing_key
signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

# ************* TASK 4: ADD SIGNING INFORMATION TO THE REQUEST *************
# The signing information can be either in a query string value or in
# a header named Authorization. This code shows how to use a header.
# Create authorization header and add to request headers
authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

# The request can include any headers, but MUST include "host", "x-amz-date",
# and (for this scenario) "Authorization". "host" and "x-amz-date" must
# be included in the canonical_headers and signed_headers, as noted
# earlier. Order here is not significant.
# Python note: The 'host' header is added automatically by the Python 'requests' library.
headers = {'Accept':'application/json',
           'x-api-key':header['x-api-key'],
           # 'Host' : 'qa-api.awseventservices.com',
           'X-Amz-Security-Token' : sessionToken,
           'x-amz-date': amzdate,
           'Authorization': authorization_header}

# ************* SEND THE REQUEST *************
request_url = endpoint + '?' + canonical_querystring

print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
print('Request URL = ' + request_url)
r = requests.get(request_url, headers=headers)

print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
print('Response code: %d\n' % r.status_code)
print(r.text)



