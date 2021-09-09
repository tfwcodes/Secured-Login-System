import hashlib
from time import sleep




while True:
    print("[1] Login")
    print("[2] Sign-Up")
    choice_system = input("Enter a choice: ")
    if choice_system == "2":

        user = input("Enter the username: ")
        password = input("Enter the password: ")
        password_confirm = input("Please confirm the password: ")
        if len(password) <= 5:
            print("Your password is too short")
            sleep(1)
            exit()
        if password == password_confirm and len(password) >= 5:

            enc_user = user.encode()
            enc_password = password.encode()

            sha256_user = hashlib.sha256(enc_user.strip()).hexdigest()

            sha256_password = hashlib.sha256(enc_password.strip()).hexdigest()

            file = open("database.txt", "w")
            file.write(sha256_user)
            file.close()

            file2 = open("password_db.txt", "w")
            file2.write(sha256_password)
            file2.close()


    if choice_system == "1":
        username = input("Enter the username: ")
        passw = input("Enter the password: ")
        file_login = open("database.txt", "r")
        line = file_login.read()



        enc_username = username.encode()
        sha256_login_user = hashlib.sha256(enc_username.strip()).hexdigest()
        if sha256_login_user != line:
            print("Username is incorrect")
            sleep(1)
            exit()
        elif sha256_login_user == line:
            print("Username is correct")

        file_pass = open("password_db.txt", "r").read()
        line3 = file_pass

        enc_pass = passw.encode()
        sha256_login_pass = hashlib.sha256(enc_pass.strip()).hexdigest()
        if sha256_login_pass != line3:
            print("Incorrect password")
            sleep(1)
            exit()
        elif sha256_login_pass == line3:
            print("Password is correct")







