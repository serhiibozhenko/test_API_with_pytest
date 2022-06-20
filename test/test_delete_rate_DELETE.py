import requests
import json
import pytest
from test_Keys import *
from test_Links import *

# 1.8/Delete put rate for movie

def test_delete_put_rateMovie():
    result6 = requests.delete(url=baseUrl+path7, params=payload)
    checkforSuccessE = result6.json()['success']
    assert checkforSuccessE == True
    checkforStatMessageE = result6.json()['status_message']
    assert checkforStatMessageE == "The item/record was deleted successfully."
    checkforStatCodeE = result6.json()['status_code']
    assert checkforStatCodeE == 13
