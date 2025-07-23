# monster
mon_1 = 100

# อาวุธ
sword = 10
axe = 25
bow = 15

while True:
    menu = int(input("ต่อสู้กับมอนสเตอร์กด 1 / ออกกด 2 : "))
    if menu == 1:
        num = int(input("จะโจมตีกี่ครั้ง : "))
        for i in range(0,num):
            choose = int(input("เลือกอาวุธ 1.ดาบ 2.ขวาน 3.ธนู : "))
            round = i + 1
            print("รอบที่ :", round)
            if choose == 1:
                mon_1 -= sword
                print("ใช้ดาบโจมตีดาเมจ = 10")
                print("มอนสเตอร์เหลือ HP :", mon_1)
            elif choose == 2:
                mon_1 -= axe
                print("ใช้ขวานโจมตีดาเมจ = 25")
                print("มอนสเตอร์เหลือ HP :", mon_1)
            elif choose == 3:
                mon_1 -= bow
                print("ใช้ธนูโจมตีดาเมจ = 15")
                print("มอนสเตอร์เหลือ HP :", mon_1)
    else :
        print("จบการทำงาน")
        break

    if mon_1 == 0:
        print("มอนสเตอร์ถูกกำจัดแล้ว")
        break
    elif mon_1 < 0:
        print("มอนสเตอร์ยังไม่ตาย")
        mon_1 = 20
        print("มอนสเตอร์เหลือ HP :", mon_1)
        break

    if round == num :
        print("เราแพ้แล้ว มอรนสเตอร์ยังมี HP :", mon_1)
        break