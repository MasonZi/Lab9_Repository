#Mason Zilch Lab 9

def encode(password):
    encoded_password = ""
    for char in password:
        # Convert the character to an integer, add 3, and then convert it back to a string
        new_char = str((int(char) + 3) % 10)
        encoded_password += new_char
    return encoded_password

def decode(password):
    decoded_password = ""
    for char in password:
        new_char = str((int(char) - 3) % 10)
        decoded_password += new_char
    return decoded_password
    
def main():
    while True:
        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        pick = int(input("Please enter an option: "))

        if pick == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        if pick == 2:
            decoded_password = decode(password)
            print(f"The encoded password is: {encoded_password}, and the original password is: {decoded_password}")
        if pick == 3:
            False
            break


if __name__ == "__main__":
    main()
