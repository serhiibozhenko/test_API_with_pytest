import json
import requests
import pytest
from test_Links import *
from test_Keys import *

# 1.7/Post rate for movie and check response

def test_post_rate_movie():
    file = open('TestData/for_rate.json')
    inputData = json.loads(file.read())
    result5 = requests.post(url = baseUrl+path6, params=payload, json=inputData)
    checkforSuccess = result5.json()['success']
    assert checkforSuccess == True
    checkforStatMessage = result5.json()['status_message']
    assert checkforStatMessage == "The item/record was updated successfully."
    checkforStatCode = result5.json()['status_code']
    assert checkforStatCode == 12
