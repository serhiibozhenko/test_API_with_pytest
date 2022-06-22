import json
import requests
import pytest
from test_Links import *
from test_Keys import *

# 1.7/Post rate for movie and check response

def test_post_rate_movie():
    file = open('TestData/for_rate.json')
    inputData = json.loads(file.read())
    response = requests.post(url = baseUrl+path_for_rate_and_delete , params=payload, json=inputData)
    checkforSuccess = response.json()['success']
    assert checkforSuccess == True
    checkforStatMessage = response.json()['status_message']
    assert checkforStatMessage == "The item/record was updated successfully."
    checkforStatCode = response.json()['status_code']
    assert checkforStatCode == 12
