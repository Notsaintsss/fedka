data_base = {
    "fedushka": "2004",
    "notsaitsss": "asdfghjkl"
}




def check_password(login, password):
    if login in data_base:
        if data_base[login] == password:
            return True
        return False




user_login = "fedushka"
count = 0
passwords = ["1", "2", 'dfs', 'ggg']

with open("pop-passwords.txt") as passwords_file:
    for line in passwords_file:
        user_password = line.strip()
        if check_password(user_login, user_password) == True:
            print(f"попытка №{count} пароль подошёл")
            break
        else:
            count+=1



