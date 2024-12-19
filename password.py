import random
import string

def generate_password(length, use_digits, use_uppercase, use_special):
    
    char_pool = string.ascii_lowercase

    if use_digits:
        char_pool += string.digits
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_special:
        char_pool += string.punctuation

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_digits = input("Include digits (y/n)? ").lower() == 'y'
    use_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
    use_special = input("Include special characters (y/n)? ").lower() == 'y'
    
    password = generate_password(length, use_digits, use_uppercase, use_special)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()
