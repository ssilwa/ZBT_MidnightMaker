import requests



r = requests.get('https://zbt-backend.herokuapp.com/api/v1/midnights/accounts', headers = {'Authorization': secret_token})

print(r.text)