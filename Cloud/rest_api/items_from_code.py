import requests
import json

barcode = 8801062012725

url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev/barcode/8801062012725"

#url = "https://www.test.com"


rs = requests.get(url)
# response code

rs_code = rs.status_code


if int(rs_code) == 200:
    print("Okay")
    rs_text = rs.text
    rs_text = json.loads(rs_text)
    print(rs_text)
else:
    print(rs_code)