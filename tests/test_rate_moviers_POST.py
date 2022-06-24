import requests
from configuration import *
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA


# 1.7/Post rate for movie and check response

def test_post_rate_movie():
    response = requests.post(BaseUrl+path_for_rate_and_delete, params=payload, json=POST_SCHEMA)
    checkforSuccess = response.json()['success']
    assert checkforSuccess == True, GlobalErrorMessages.WRONG_STATUS_CODE.value
    checkforStatMessage = response.json()['status_message']
    assert checkforStatMessage == "The item/record was updated successfully.", GlobalErrorMessages.WRONG_STATUS_CODE.value
    checkforStatCode = response.json()['status_code']
    assert checkforStatCode == 12, GlobalErrorMessages.WRONG_STATUS_CODE.value

