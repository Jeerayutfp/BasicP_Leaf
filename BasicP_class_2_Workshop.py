km = int(input("ระยะทางขนส่ง : "))
print("ระยะทางขนส่งของคุณคือ :", km)
if km >= 5 and km <= 50:
    sum = 10
elif km >= 51 and km <= 100:
    sum = 15
elif km >= 101 and km <=300: 
    sum = 25
elif km >= 301 and km <=500:
    sum = 35
elif km > 500:
    sum = 45
else :
    sum = 0
    print("ไม่สามารถขนส่งได้")
print("ค่าขนส่งของคุณคือ :", sum ," บาท")