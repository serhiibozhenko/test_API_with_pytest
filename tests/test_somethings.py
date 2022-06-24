# import requests
# from configuration import SERVISE_URL
# from src.enums.global_enums import GlobalErrorMessages
#
# def test_fhsg():
#     response = requests.get(url = SERVISE_URL)
#     assert response.status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value
#     print(response.json())