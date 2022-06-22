import re
from urllib import response
import requests
from test_Keys import *
from test_Links import *
import pytest

#1.1/Simular movies not founded movie_id

def test_get_notfounded_movie():
    response = requests.get(baseUrl + path_for_check_notfounded_movie, params=payloadforGET)
    checkStatusCode = (response.json()['status_code'])
    assert checkStatusCode == 34
    forCheckSuccessStatus = (response.json()['success'])
    assert forCheckSuccessStatus == False
    fortCheckStatusMessage = (response.json()['status_message'])
    assert fortCheckStatusMessage == 'The resource you requested could not be found.'


#1.2/Simular movies not founded api_key

def test_get_notfounded_api_key():
    response = requests.get(baseUrl + path_for_check_notfounded_api_key)
    forCheckStatusCode = (response.json()['status_code'])
    assert forCheckStatusCode == 7
    assert response.status_code == 401
    assert response.json()['success'] == False
    assert response.json()['status_message'] == 'Invalid API key: You must be granted a valid key.'


#1.3/Simular movies check time for response

def test_get_check_time_response():
    response = requests.get(baseUrl + check_time_for_response, params=payloadforGET)
    timeResp= response.elapsed.total_seconds()
    assert timeResp <= 1

# #1.4/Simular movies check header have value

def test_get_check_header_value_response():
    response = requests.get(baseUrl + check_header_value_response, params=payloadforGET)
    checkHeader = response.headers['content-type']
    assert checkHeader == 'application/json;charset=utf-8'
