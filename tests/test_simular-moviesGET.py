import requests
from configuration import *
from src.enums.global_enums import GlobalErrorMessages


#1.1/Simular movies not founded movie_id

def test_get_notfounded_movie():
    response = requests.get(BaseUrl+path_for_check_notfounded_movie, params=payloadforGET)
    checkStatusCode = (response.json()['status_code'])
    assert checkStatusCode == 34, GlobalErrorMessages.WRONG_STATUS_CODE.value
    forCheckSuccessStatus = (response.json()['success'])
    assert forCheckSuccessStatus == False, GlobalErrorMessages.WRONG_STATUS_CODE.value
    fortCheckStatusMessage = (response.json()['status_message'])
    assert fortCheckStatusMessage == 'The resource you requested could not be found.'


#1.2/Simular movies not founded api_key

def test_get_notfounded_api_key():
    response = requests.get(BaseUrl + path_for_check_notfounded_api_key)
    forCheckStatusCode = (response.json()['status_code'])
    assert forCheckStatusCode == 7, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['success'] == False, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['status_message'] == 'Invalid API key: You must be granted a valid key.', GlobalErrorMessages.WRONG_STATUS_CODE.value


#1.3/Simular movies check time for response

def test_get_check_time_response():
    response = requests.get(BaseUrl + check_time_for_response, params=payloadforGET)
    timeResp = response.elapsed.total_seconds()
    assert timeResp <= 1, GlobalErrorMessages.WRONG_STATUS_CODE.value

# #1.4/Simular movies check header have value/

def test_get_check_header_value_response():
    response = requests.get(BaseUrl + check_header_value_response, params=payloadforGET)
    checkHeader = response.headers['content-type']
    assert checkHeader == 'application/json;charset=utf-8', GlobalErrorMessages.WRONG_STATUS_CODE.value
