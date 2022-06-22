from ast import Str
from lib2to3.pgen2.token import STRING
from typing import Dict
import requests
import pytest

from test_Keys import *
from test_Links import *


# 1.5/Get details about movie

def test_get_detail_movie():
    response = requests.get(url = baseUrl + path_for_check_detail, params=payloadforGET)
    checkforString = response.json()['original_title']
    assert type(checkforString) == str
    checkforDict = response.json()
    assert type(checkforDict) == dict