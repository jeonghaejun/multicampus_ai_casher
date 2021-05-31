import requests
import json

print("Scan the barcode")
while True:
    scan_in = input("Input :")
    if scan_in is 'q':   # 키보드에서 q 누르고 enter입력하면 종료
        break    
    print("result : " + scan_in)
    

    barcode = scan_in

    url = "https://475pko0wjc.execute-api.eu-west-2.amazonaws.com/dev/barcode/"+ barcode

    #url = "https://www.test.com"


    rs = requests.get(url)
    # response code

    rs_code = rs.status_code


    if int(rs_code) == 200:
        print("Okay")
        rs_text = rs.text
        rs_text = json.loads(rs_text)
        rs_item = rs_text['body'] 
        product = json.loads(rs_item)
        product["Qty"] = 1
        print(product)

        
    else:
        print(rs_code)
