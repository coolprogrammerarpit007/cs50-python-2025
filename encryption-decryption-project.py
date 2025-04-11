# Encryption - Decryption PROJECT

text = input("Enter World you want to encrypt: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
custom_key = 'cryptography'
def cryptography(message,key,direction = 1):
    encrypted_message = ''
    key_index = 0
    for char in message.lower():
        if not char.isalpha():
            encrypted_message += char
        else:
            key_char = key[key_index%len(key)]
            key_index += 1
            offset  = alphabet.index(key_char)
            index = alphabet.find(char)
            encrypted_message += alphabet[(index + direction * offset) % len(alphabet)]
    return encrypted_message
    

encrypted_data = cryptography(text,custom_key)
print("Encrypted String: ",encrypted_data)
decrypted_data = cryptography(encrypted_data,custom_key,-1)
print("Decrypted String: ",decrypted_data)