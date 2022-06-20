import requests
from test_Keys import api_key
from test_Links import *

#1.1/Simular movies not founded movie_id

result = requests.get(url1, api_key)
forAssert = (result.json()['status_code'])
print('Status code - '+ str(result.status_code))
if forAssert == 34:
    print('Passed test - Simular movies not founded movie_id')
else:
    print('Not passed test')

forAssertSuccess = (result.json()['success'])

if forAssertSuccess == False:
    print('Success is false')
else:
    print('Not passed test')

forAssertStatusMessage = (result.json()['status_message'])

assert 'The resource you requested could not be found.' == forAssertStatusMessage 

#1.2/Simular movies not founded api_key

result1 = requests.get(url2)
print(result1.json()) 
forAssert1 = (result1.json()['status_code'])
assert forAssert1 == 7
assert result1.status_code == 401
assert result1.json()['success'] == False
assert result1.json()['status_message'] == 'Invalid API key: You must be granted a valid key.'
print('Test -  Simular movies not founded api_key - Passed')


#1.3/Simular movies time for response

result2 = requests.get(url3, api_key)
timeResp= result2.elapsed.total_seconds()

passedTimeforRes = int(timeResp)

if passedTimeforRes <= 2:
    print('Passed test time for response')
    print(timeResp)
else:
    print('Not passed test time for response')
    print(timeResp)


#1.4/Simular movies check header have value

result3 = requests.get(url4, api_key)
checkHeader = result3.headers['content-type']
assert checkHeader == 'application/json;charset=utf-8'
print('Passed test check header have value')
