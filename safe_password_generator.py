from random import *

digits = '0123456789'
low_case = 'abcdefghijklmnopqrstuvwxyz'
up_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
specials = '!#$%&*+-=?@^_'
chars = []

print('Добро поаловать в генератор безопасных паролей!')

#---------------------------------------запрос данных у пользователя
quantity = input('Введите количество паролей для генерации: ')
while quantity.isdigit() != True:
    quantity = input('Попробуйте снова: ')
quantity = int(quantity)

length = input('Укажите длину пароля: ')
while length.isdigit() != True:
    length = input('Попробуйте снова: ')
length = int(length)

def yes_no_check(s):
    while s.lower().strip() not in 'данет':
        print('Надо ввести "да" или "нет"!')
        s = input('Попробуйте снова: ')
    return s

digs = yes_no_check(input('Включать цифры? (да, нет): ').strip())
ups = yes_no_check(input('Включать прописные буквы? (да, нет): ').strip())
lows = yes_no_check(input('Включать строчные буквы? (да, нет): ').strip())
specs = yes_no_check(input('Включать символы !#$%&*+-=?@^_? (да, нет): ').strip())
wtf = yes_no_check(input('Исключить неоднозначные символы - il1oO0? (да, нет):').strip())

#---------------------------------------наполнение списка символами
if wtf == 'да':
    for c in 'il1oO0':
        if c == '0' or c == '1':
            digits = digits.replace(c, '')
        elif c == 'O':
            up_case = up_case.replace(c, '')
        else:
            low_case = low_case.replace(c, '')
if digs == 'да':
    chars.append(digits)
if ups == 'да':
    chars.append(up_case)
if lows == 'да':
    chars.append(low_case)
if specs == 'да':
    chars.append(specials)

# --------------------------------------генерация пароля
def generate_password_2(length):
    password = ''
    while len(password) != length:
        password += choice(chars[randint(0, len(chars)-1)])
    return password

#---------------------------------------вывод пароля
for _ in range(quantity):
    print(generate_password_2(length))
