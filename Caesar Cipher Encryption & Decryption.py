print("\n*************************************")
def caesar_cipher(text, shift, decrypt=False):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97) if not decrypt else chr(((ord(char) - 97 - shift) % 26) + 97)
            else:
                shifted_char = chr(((ord(char) - 65 + shift) % 26) + 65) if not decrypt else chr(((ord(char) - 65 - shift) % 26) + 65)
        else:
            shifted_char = char
        encrypted_text += shifted_char
    return encrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt (e) or decrypt (d) or quit (q)? ").lower()
        if choice == 'q':
            print("Exiting the program...")
            break
        elif choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption, 'd' for decryption, or 'q' to quit.")
            continue
        
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
            print("-------------------------------------------\n")
        else:
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, decrypt=True)
            print("Decrypted message:", decrypted_message)
            print("-------------------------------------------\n")

if __name__ == "__main__":
    main()
