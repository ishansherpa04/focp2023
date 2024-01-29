from pass_enc import read_passwords, write_passwords, encrypt_password

def change_password():
    passwords = read_passwords()

    usernames = [user[0] for user in passwords]
    
    username = input("User: ").lower()
    
    user_index = -1
    for i in range(len(passwords)):
        if passwords[i][0] == username:
            user_index = i
            break

    if user_index == -1:
        print("User not found.")
        return

    current_password = input("Current Password: ")
    new_password = input("New Password: ")
    confirm_password = input("Confirm: ")

    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    encrypted_current_password = encrypt_password(current_password)

    if passwords[user_index][2] == encrypted_current_password:
        passwords[user_index] = (username, passwords[user_index][1], encrypt_password(new_password))
        write_passwords(passwords)
        print("Password changed.")
    else:
        print("Invalid current password.")

if __name__ == "__main__":
    change_password()
