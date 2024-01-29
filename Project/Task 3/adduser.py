from pass_enc import read_passwords, write_passwords, encrypt_password

def add_user():
    usernames = [user[0] for user in read_passwords()]
    
    new_username = input("Enter new username: ").lower()
    
    if new_username in usernames:
        print("Unable to add user. The username may already exists.")
        return

    real_name = input("Enter real name: ")
    password = input("Enter password: ")

    encrypted_password = encrypt_password(password)
    
    passwords = read_passwords()
    passwords.append((new_username, real_name, encrypted_password))
    
    write_passwords(passwords)
    print("User Created.")

if __name__ == "__main__":
    add_user()
