from pass_enc import read_passwords, encrypt_password

def login():
    usernames = [user[0] for user in read_passwords()]
    
    username = input("User: ").lower()
    
    if username not in usernames:
        print("Access denied.")
        return

    password = input("Password: ")
    encrypted_password = encrypt_password(password)

    for user in read_passwords():
        if user[0] == username and user[2] == encrypted_password:
            print("Access granted.")
            return

    print("Access denied.")

if __name__ == "__main__":
    login()
