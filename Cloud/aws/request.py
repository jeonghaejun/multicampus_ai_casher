import json
import requests
#
# datas = {
#   "result": 0,
#   "time": 1456839299,
#   "item": [
#     {
#       "outcome": 1,
#       "id": 10864,
#       "prob": 0.7957403659820557
#     },
#     {
#       "outcome": 0,
#       "id": 10865,
#       "prob": 0.7957403659820557
#     },
#     {
#       "outcome": 1,
#       "id": 10866,
#       "prob": 0.7957403659820557
#     }
#   ]
# }
#
# url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev/judgement"
#
# response = requests.post(url, data=json.dumps(datas))

url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev"

response = requests.get(url)
