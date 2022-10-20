logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(text, shift, direction):
    cipher_text = ""
    for ch in text:
        if ch == ' ':
            cipher_text += ' '
            continue
        position = alphabet.index(ch)
        if direction == 'encode':
            new_position = position + shift
            if new_position > 25:
                new_position = new_position - 26
        else:
            new_position = position - shift
            if new_position < 0:
                new_position = 26 + new_position
        cipher_text += alphabet[new_position]
    return cipher_text


def input_take():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    while True:
        try:
            shift = int(input("Type the shift number (1-25):\n"))
        except ValueError:
            print("Invalid shift number. Please enter a valid shift number.")
            continue
        else:
            break
    if direction != 'encode' and direction != 'decode':
        print("Please enter 'encode' or 'decode'")
        input_take()
    if shift < 0 or shift > 26:
        print("Shift number must be between 0 and 26")
        input_take()
    result = caesar_cipher(text, shift, direction)
    print(f"Your {direction} message is: {result}\n")
    is_continue = input("Do you want to continue? (y/n):\n")
    if is_continue.lower() == 'y':
        input_take()
    else:
        return


if __name__ == "__main__":
    print(logo)
    input_take()
