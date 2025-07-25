# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    print (movie_list[{"movie_name", "ticket_price", "genre", "age_restriction"}])

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age, age_restriction):
    # TODO: ถ้า age_restriction เป็น 'G' ให้ผ่านเลย
    # ถ้าไม่ใช่ ให้ดึงเลขอายุขั้นต่ำมาเปรียบเทียบกับ user_age
    if age_restriction == 'G':
        return True
    else:
        if user_age >= int(age_restriction):
            return True
        else:
            return False

# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    if genre == 'Horror':
        return base_price + 50
    else:
        return base_price

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    # TODO: 
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    # 3. รับอายุผู้ใช้
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
    choose = int(input("เลือกหนัง (1-5): "))
    user_age = int(input("กรุณากรอกอายุของคุณ: "))

    if not check_age(user_age, movie_list[choose]['age_restriction']):
        print("คุณอายุน้อยเกินไป")
        return
    soundtrack_choice = int(input("เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack): "))
    print(calculate_price(movie_list[choose]['ticket_price'], movie_list[choose]['genre']))
    print("คุณได้ซื้อบัตรชมหนัง", movie_list[choose]['movie_name'], movie_list[choose]['soundtrack_choice'], "ในราคา", calculate_price(movie_list[choose]['ticket_price'], movie_list[choose]['genre']), "บาท")

    return movie_list

def main():
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]

    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    print("1. แสดงหนังทั้งหมด")
    print("2. ซื้อตั๋วหนัง")

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    menu = input("เลือกเมนู: ")

    # TODO: ตรวจสอบเมนูที่เลือก
    if menu == '1':
        show_movies()
    elif menu == '2':
        buy_ticket()
    else :
        print("เมนูไม่ถูกต้อง")

# เรียก main เพื่อเริ่มโปรแกรม
main()