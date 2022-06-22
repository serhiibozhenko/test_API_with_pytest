import requests
import json
import pytest
from test_Keys import *
from test_Links import *

# 1.8/Delete put rate for movie

def test_delete_put_rateMovie():
    response = requests.delete(url=baseUrl+path_for_rate_and_delete, params=payload)
    checkforSuccessE = response.json()['success']
    assert checkforSuccessE == True
    checkforStatMessageE = response.json()['status_message']
    assert checkforStatMessageE == "The item/record was deleted successfully."
    checkforStatCodeE = response.json()['status_code']
    assert checkforStatCodeE == 13
