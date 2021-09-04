import requests


chat_id='Replace your chat id here'
token='Replace your token here'
base_url='https://api.telegram.org/bot{}/sendPhoto?chat_id={}'.format(token,chat_id)
fname='give name of the file you want to send'
files={'photo':open(fname,'rb')}
resp=requests.post(base_url,files=files)
print(resp)
print(resp.status_code)
