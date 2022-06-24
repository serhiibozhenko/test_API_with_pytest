import requests
from configuration import *
from src.enums.global_enums import GlobalErrorMessages

# 1.5/Get details about movie

def test_get_detail_movie():
    response = requests.get(BaseUrl + path_for_check_detail, params=payloadforGET)
    checkforString = response.json()['original_title']
    assert type(checkforString) == str, GlobalErrorMessages.WRONG_STATUS_CODE.value
    checkforDict = response.json()
    assert type(checkforDict) == dict, GlobalErrorMessages.WRONG_STATUS_CODE.value