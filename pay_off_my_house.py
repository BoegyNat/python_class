
def convert_Int_to_stringWithComma(price) :
    return "{:,}".format(price)

print("ระบบคำนวนการชำระผ่อนค่าบ้าน")
mode = input("เลือกโหมดที่ต้องการ (1:หาระยะเวลา , 2:หายอดค้างชำระ) : ")
if mode == "1" :
    print("หาระยะเวลา")
    price = int(input("ราคาบ้าน หรือ ยอดเงินกู้คงเหลือ : "))
    money = int(input("เงินผ่อนต่อเดือน : "))
    rate = float(input("อัตราดอกเบี้ยต่อปี : "))

    rate_per_month = rate / 100 / 12
    price_init = price
    month = 0
    total_pay = 0
    while price > 0 :
        if month % 12 == 0 :
            print("\033[93m----------------------------------------------\033[0m")
            print(f"\033[93m    ปีที่ {month // 12 + 1}\033[0m")
        price = price * (1 + rate_per_month)
        print(f"\033[92m    เดือนที่ {month + 1} : \033[0m")
        if(price > money) :
            price -= money
            total_pay += money
            print(f"        ต้องชำระ {convert_Int_to_stringWithComma(money)} บาท")
        else :
            total_pay += price
            print(f"        ต้องชำระ {convert_Int_to_stringWithComma(price)} บาท")
            price = 0
        print(f"        ยอดค้างชำระ {convert_Int_to_stringWithComma(price)} บาท")
        month += 1
    
    print("\033[93m/////--------------------------------------------/////\033[0m")
    print()
    print(f"\033[93m    ต้องชำระเป็นเวลาทั้งหมด {month // 12} ปี {month % 12} เดือน\033[0m")
    print(f"\033[93m    ยอดรวมที่ชำระทั้งหมด {convert_Int_to_stringWithComma(total_pay)} บาท\033[0m")
    print(f"\033[93m    ยอดรวมดอกเบี้ยที่ต้องชำระ {convert_Int_to_stringWithComma(total_pay - price_init )} บาท\033[0m")
    print()
    print("\033[93m/////--------------------------------------------/////\033[0m")

elif mode == "2" :
    print("หายอดค้างชำระ")
    price = int(input("ราคาบ้าน หรือ ยอดเงินกู้คงเหลือ : "))
    money = int(input("เงินผ่อนต่อเดือน : "))
    rate = float(input("อัตราดอกเบี้ยต่อปี : "))
    time = int(input("จำนวนเดือนที่ต้องการชำระ : "))

    rate_per_month = rate / 100 / 12

    total_pay = 0
    for i in range(time) :
        price = price * (1 + rate_per_month)
        if(price > money) :
            price -= money
            total_pay += money
        else :
            price = 0
            total_pay += price

    print("\033[93m/////--------------------------------------------/////\033[0m")
    print()
    print(f"\033[93m    ยอดรวมที่ชำระได้ {convert_Int_to_stringWithComma(total_pay)} บาท\033[0m")
    print(f"\033[93m    ยอดค้างชำระ {convert_Int_to_stringWithComma(price)} บาท\033[0m")
    print()
    print("\033[93m/////--------------------------------------------/////\033[0m")
