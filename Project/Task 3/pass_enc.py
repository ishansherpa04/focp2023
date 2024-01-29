def rot13_encode(text):
    result = ''
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

PASSWORD_FILE = "passwd.txt"

def read_passwords():
    try:
        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()

        passwords = [tuple(line.strip().split(":")) for line in lines if line.strip()]
        return passwords
    except FileNotFoundError:
        return []

def write_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        for username, real_name, encrypted_password in passwords:
            file.write(f"{username}:{real_name}:{encrypted_password}\n")

def encrypt_password(password):
    encoded_password = rot13_encode(password)
    return encoded_password
