import requests
from configuration import *
from src.enums.global_enums import GlobalErrorMessages

# 1.8/Delete put rate for movie

def test_delete_put_rateMovie():
    response = requests.delete(BaseUrl+path_for_rate_and_delete, params=payload)
    checkforSuccessE = response.json()['success']
    assert checkforSuccessE == True, GlobalErrorMessages.WRONG_STATUS_CODE.value
    checkforStatMessageE = response.json()['status_message']
    assert checkforStatMessageE == "The item/record was deleted successfully.", GlobalErrorMessages.WRONG_STATUS_CODE.value
    checkforStatCodeE = response.json()['status_code']
    assert checkforStatCodeE == 13, GlobalErrorMessages.WRONG_STATUS_CODE.value
