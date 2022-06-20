from ast import Str
from lib2to3.pgen2.token import STRING
from typing import Dict
import requests

from test_Keys import *
from test_Links import *


# 1.5/Get details about movie

def test_get_detail_movie():
    result4 = requests.get(url = baseUrl + path5, params=payloadforGET)
    checkforString = result4.json()['original_title']
    assert type(checkforString) == str
    # checkforDict = result4.json()
    # assert type(checkforDict) == Dict