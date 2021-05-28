print("Scan the barcode")
while True:
    scan_in = input("Input :")
    if scan_in is 'q':   # 키보드에서 q 누르고 enter입력하면 종료
        break    
    print("result : " + scan_in)