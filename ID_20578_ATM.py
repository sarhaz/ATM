balance = 500000000.0
pin_code = 1914
bankomatda_bor_summa = 500000000


def ortga():
    """xizmatlar bo'limiga o'tish yoki tilni o'zgartirish bo'limiga o'tish"""
    back = input("""
        0.xizmatlar bo'limiga qaytish
        9.boshqa tilni tanlash
        """)
    if back == "0":
        return uzbekcha()
    elif back == "9":
        return Til_tanlash()
    else:
        print("noto'g'ri raqam kiritdingiz")
        return ortga()


def hisob_raqamni_korish():
    """hisob raqamni ko'rish uchun funksiya"""
    print(f"{balance} so'm pulingiz bor")
    return ortga()


def naqd_pul_olish():
    """Bu, naqd pul olish funksiyasi"""
    global balance
    pul = int(input("qancha pul olmoqchiligizni kiriting: "))
    a = pul % 1000
    if pul >= 1000 and a == 0:
        balance = balance - pul * 1.01
        if pul >= 500000000:
            print(f"bizning bankomatda {pul} summa yo'q")
        if balance >= 0:
            print(f"kartangizdan {pul * 1.01}  so'm pul olindi")
            print(f"qolgan pul miqdori {balance} so'm")
        if bankomatda_bor_summa < 0:
            print("bizning bankomatda pul qolmadi.Boshqa xizmatlardan foydalanishingiz mumkin")
            return uzbekcha()
    else:
        print("bizning bankomat 1000 so'mdan mayda pullarni berolmaydi")
        return naqd_pul_olish()
    return ortga()


def pin_kodni_ozgartirish():
    """Bu, pin kodni o'zgartirish funksiyasi"""
    new_pin_code = int(input("yangi pin kodni kiriting va u 4 xonali bo'lishi shart:"))
    if 1000 <= new_pin_code <= 9999:
        pin_code = new_pin_code
        print(f"kodingiz {pin_code}ga o'zgardi")
    else:
        print("siz 4 xonali son kiritmagansiz  ")
        return pin_kodni_ozgartirish()
    return ortga()


def kartaga_pul_utqazish():
    """Bu ,kartaga pul utqazish funksiyasi"""
    global balance
    pul = int(input("qancha pul yuklamoqchi bulsangiz qiymatini kiriting:"))
    a = pul % 1000
    if a == 0:
        balance += pul
        print(f"balansingizdagi pul miqdori {balance} so'm buldi")
        return ortga()
    else:
        print("to'g'ri qiymat kirgizing")
        return kartaga_pul_utqazish()


def uzbekcha():
    """Bu, o'zbek tili uchun xizmat tanlash funsiyasi"""
    print("xizmatlar:>>")
    xizmatlar = input("""
    1.HISOB RAQAMINI KO'RISH
    2.PUL YECHIB OLISH
    3.PAROLNI UZGARTIRISH
    4.KARTAGA PUL TASHASH
    9.TILNI O'ZGARTIRISH
    """)
    if xizmatlar == "1":
        return hisob_raqamni_korish()
    elif xizmatlar == "2":
        return naqd_pul_olish()
    elif xizmatlar == "3":
        return pin_kodni_ozgartirish()
    elif xizmatlar == "4":
        return kartaga_pul_utqazish()
    elif xizmatlar == "9":
        return Til_tanlash()
    else:
        print("noto'g'ri raqamni kiritdingiz!")
        return uzbekcha()


def pin_kod():
    for i in range(0, 3):
        pin = int(input("pin kodni tering: "))
        if pin == pin_code:
            print("Kod tasdiqlandi ")
            return uzbekcha()
        elif i == 2 and pin != pin_code:
            print("block")
        elif pin != pin_code:
            print("Xato kod")


def reply():
    """Switch to the services section or language change section"""
    back = input("""
        0. Return to services
        9. Choose another language
        """)
    if back == "0":
        return choose_service()
    elif back == "9":
        return Til_tanlash()
    else:
        print("You entered an incorrect number")
        return reply()


def check_balance():
    """Function to check the account balance"""
    print(f"Your balance is {balance} UZS")
    return reply()


def withdraw_cash():
    """This is the cash withdrawal function"""
    global balance
    amount = int(input("Enter the amount you want to withdraw: "))
    a = amount % 1000
    if amount >= 1000 and a == 0:
        balance = balance - amount * 1.01
        if amount >= 500000000:
            print(f"Our ATM does not have {amount * 1.01} UZS")
        if balance >= 0:
            print(f"{amount} UZS withdrawn from your card")
            print(f"Remaining balance: {balance} UZS")
        if bankomatda_bor_summa < 0:
            print("There is no money left in our ATM. You can use other services.")
            return choose_service()
    else:
        print("Our ATM does not dispense amounts less than 1000 UZS")
        return withdraw_cash()
    return reply()


def change_pin():
    """This is the function to change the PIN code"""
    new_pin_code = int(input("Enter the new PIN code, which must be 4 digits: "))
    if 1000 <= new_pin_code <= 9999:
        pin_code = new_pin_code
        print(f"Your code has been changed to {pin_code}")
    else:
        print("You did not enter a 4-digit number")
        return change_pin()
    return reply()


def deposit_money():
    """This is the function to deposit money into the card"""
    global balance
    amount = int(input("Enter the amount you want to load onto the card: "))
    a = amount % 1000
    if a == 0:
        balance += amount
        print(f"The amount of money in your balance is {balance} UZS now")
        return reply()
    else:
        print("you didn't enter proper amount")
        return deposit_money()


def choose_service():
    """Function to select a service for the Uzbek language"""
    print("Services: >>")
    services = input("""
    1. CHECK BALANCE
    2. WITHDRAW CASH
    3. CHANGE PASSWORD
    4. DEPOSIT MONEY TO CARD
    9.CHANGING LANGUAGE
    """)
    if services == "1":
        return check_balance()
    elif services == "2":
        return withdraw_cash()
    elif services == "3":
        return change_pin()
    elif services == "4":
        return deposit_money()
    elif services == "9":
        return Til_tanlash()
    else:
        print("You entered the wrong number!")
        return choose_service()


def enter_pin():
    for i in range(0, 3):
        pin = int(input("Enter the PIN code: "))
        if pin == pin_code:
            print("Code confirmed")
            return choose_service()
        elif i == 2 and pin != pin_code:
            print("Blocked")
        elif pin != pin_code:
            print("Incorrect code")


def ответ():
    """Переключение в раздел услуг или раздел смены языка"""
    back = input("""
        0. Вернуться к услугам
        9. Выбрать другой язык
        """)
    if back == "0":
        return выбрать_сервис()
    elif back == "9":
        return Til_tanlash()
    else:
        print("Вы ввели неправильный номер")
        return ответ()


def проверить_баланс():
    """Функция для проверки баланса счета"""
    print(f"Ваш баланс составляет {balance} UZS")
    return ответ()


def снять_денги():
    """Это функция снятия наличных"""
    global balance
    amount = int(input("Введите сумму, которую вы хотите снять: "))
    a = amount % 1000
    if amount >= 1000 and a == 0:
        balance = balance - amount * 1.01
        if amount >= 500000000:
            print(f"У нашего банкомата нет {amount * 1.01} UZS")
        if balance >= 0:
            print(f"{amount} UZS снято с вашей карты")
            print(f"Остаток на счету: {balance} UZS")
        if bankomatda_bor_summa < 0:
            print("В нашем банкомате не осталось денег. Вы можете воспользоваться другими услугами.")
            return выбрать_сервис()
    else:
        print("Наш банкомат не выдаёт суммы менее 1000 UZS")
        return withdraw_cash()
    return ответ()


def изменить_пароль():
    """Это функция для изменения PIN-кода"""
    new_pin_code = int(input("Введите новый PIN-код, который должен состоять из 4 цифр: "))
    if 1000 <= new_pin_code <= 9999:
        pin_code = new_pin_code
        print(f"Ваш код был изменен на {pin_code}")
    else:
        print("Вы не ввели 4-х значное число")
        return изменить_пароль()
    return ответ()


def внести_на_карту():
    """Это функция для внесения денег на карту"""
    global balance
    amount = int(input("Введите сумму, которую вы хотите внести на карту: "))
    a = amount % 1000
    if a == 0:
        balance += amount
        print(f"Сумма денег на вашем счету теперь составляет {balance} UZS")
        return ответ()
    else:
        print("Вы не ввели правильное количество")
        return внести_на_карту()


def выбрать_сервис():
    """Функция выбора услуг для узбекского языка"""
    print("Услуги: >>")
    services = input("""
    1. ПРОВЕРИТЬ БАЛАНС
    2. СНЯТЬ ДЕНЬГИ
    3. ИЗМЕНИТЬ ПАРОЛЬ
    4. ВНЕСТИ ДЕНЬГИ НА КАРТУ
    9.ИЗМЕНИТЬ ЯЗЫК
    """)
    if services == "1":
        return проверить_баланс()
    elif services == "2":
        return снять_денги()
    elif services == "3":
        return изменить_пароль()
    elif services == "4":
        return внести_на_карту()
    elif services == "9":
        return Til_tanlash()
    else:
        print("Вы ввели неверный номер!")
        return выбрать_сервис()


def Введите_PIN():
    for i in range(0, 3):
        pin = int(input("Введите PIN-код: "))
        if pin == pin_code:
            print("Код подтвержден")
            return выбрать_сервис()
        elif i == 2 and pin != pin_code:
            print("Заблокировано")
        elif pin != pin_code:
            print("Неверный код")


def Til_tanlash():
    """Bu ,foydalanuvchi tushunadigan tilni tanlash funksiyasi """
    print("""
    iltimos, tilni tanlang
    пожалуйста, выберите язык
    please, choose the language>>>>>>""")
    til = input("""
    1.O'ZBEK 
    2.РУССКИЙ
    3.ENGLISH
    4.QUIT
    --->""")

    if til == "1":
        return pin_kod()
    elif til == "2":
        return Введите_PIN()
    elif til == "3":
        return enter_pin()
    elif til == "4":
        print("""
        foydalanganingiz uchun rahmat , kartangizni olishingiz mumkin
        Thank you for using, you can get your card
        Спасибо за использование, вы можете взять свою карту.
        """)
    else:
        print("noto'g'ri raqam kiritdingiz")
    return Til_tanlash()


if __name__ == "__main__":
    Til_tanlash()
