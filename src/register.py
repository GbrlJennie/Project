monsterAwal = ["Pikachow", "Bulbu", "Zeze", "Zuko", "Chacha"]
validUsername = True
notExistUsername = True

def read_csv(file_path):
    data = []
    row = []
    field = ""
    in_quotes = False

    with open(file_path, 'r') as file:
        for char in file.read():
            if char == ';' and not in_quotes:
                char = ','
                row.append(field)
                field = ""
            elif char == '"' and not in_quotes:
                in_quotes = True
            elif char == '"' and in_quotes:
                in_quotes = False
            elif char == '\n' and not in_quotes:
                row.append(field)
                data.append(row)
                row = []
                field = ""
            else:
                field += char

    if field:
        row.append(field)
        data.append(row)

    return data

user_pas = read_csv('user.csv')

def isUsernameValid(username):
    valid = True
    tempUsername = [char for char in username]
    for i in tempUsername:
        if (ord(i) >= 0 and ord(i) <= 47 and ord(i) != 45) or (ord(i) > 57 and ord(i) < 65) or (ord(i) > 90 and ord(i) != 95 and ord(i) < 97) or ord(i) > 122:
            valid = False
            break
    return (valid)


def isUsernameExist(username, user_pas):
    valid = True
    tempList = []
    for i in range(len(user_pas)):
        for j in range(len(user_pas)):
            if j == 1:
                tempList.append(user_pas[i][j])
    print(tempList)
    for i in tempList:
        if username == i:
            valid = False
            break
    print(valid)
    return (valid)


def Register():
    role = 'agent'
    oc = 0

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    print()

    validUsername = isUsernameValid(username)
    while validUsername == False:
        print("Username hanya boleh berisi alfabet, angka, underscore, dan strip")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        validUsername = isUsernameValid(username)

    notExistUsername = isUsernameExist(username, user_pas)
    while notExistUsername == False:
        print(
            f"Username {username} sudah terpakai, silahkan gunakan username lain!")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print()
        notExistUsername = isUsernameExist(username, user_pas)

    # ini temporary, ntar pas save lgsg ngewrite ke csv
    cnt = len(user_pas)
    tempUserpasList = []
    tempUserpas = str(cnt)+";"+username+";"+password+";"+role+";"+str(oc)
    tempUserpasList.append(tempUserpas)

    # Buat save nanti
    # f = open('user.csv', 'a')
    # for i in tempUserpasList:
    #   f.write("\n"+i)
    # f.close()

    print("Silahkan pilih salah satu monster sebagai monster awalmu.")
    print("1. Pikachow")
    print("2. Bulbu")
    print("3. Zeze")
    print("4. Zuko")
    print("3. Chacha")
    print()
    angkaMonster = int(input("Monster pilihanmu: "))
    monster = monsterAwal[angkaMonster-1]

    print(
        f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster}!")

Register()