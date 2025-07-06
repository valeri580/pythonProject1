password_true = 'qwerty123'
password = ""
count = 0

while password != password_true :
    if count < 3:
        password = input ('Введите пароль - ')
        count += 1
    else:
        print('Доступ  не разрешен')
        break
if  password == password_true:
    print('Доступ разрешен')