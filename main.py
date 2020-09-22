import requests

url = 'https://www.wrike.com/api/v4/contacts'
access_token = '<token>'
authHeader = "bearer "+access_token

params = {
    "Authorization":authHeader
    ,'Accept':'application/json'
}

try:
    response = requests.get(url,headers=params)
    if response.status_code == 200:
        print(f'Success! Response = {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Woops, there is a request error {response.status_code}')
except Exception as e:
    print(f'There is an error {e}')
print('Program ended')
