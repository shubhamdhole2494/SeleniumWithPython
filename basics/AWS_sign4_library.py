import json

import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth

url = 'https://qa-api.awseventservices.com/events/reinvent-20/users/'
header = {'x-api-key': 'mwISZeE0fMvjX7aZUAZbVY97Zx5qamgUWRg9obI3'}
print(header['x-api-key'])
header1 = {
    'Content-Type': 'application/json',
    'Accept': 'ver=1.0',
    'x-api-key': 'mwISZeE0fMvjX7aZUAZbVY97Zx5qamgUWRg9obI3',
    'Host': 'qa-api.awseventservices.com',
    'User-Agent': 'PostmanRuntime/7.24.1',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Content-Length': '952',
    'Postman-Token': '1b940cd2-6e03-4ef6-b439-0f674b691f67'

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

auth = AWSRequestsAuth(aws_access_key=accessKeyId,
                       aws_secret_access_key=secretAccessKey,
                       aws_token=sessionToken,
                       aws_host='qa-api.awseventservices.com',
                       aws_region='us-east-1',
                       aws_service='execute-api')

r = requests.get('https://qa-api.awseventservices.com/events/reinvent-20/sessions/catalog', headers=header, auth=auth)
print(r.text)
