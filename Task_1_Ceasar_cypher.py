
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def Encrypt(Plaintext, key):
    Ciphertext = ''
    for letter in Plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                Ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                Ciphertext += letters[new_index]
    return Ciphertext

def Decrypt(Ciphertext, key):
    Plaintext = ''
    for letter in Ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                Plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                Plaintext += letters[new_index]
    return Plaintext

print()
print('**TASK 1:- CEASAR CIPHER PROGRAM**')
print()

print('Do you Want to Encrypt or Decrypt')
user_input = input('e/d: ').lower()
print()

if user_input =='e':
    print('Encryption mode selected')
    print()
    key = int(input('Enter the key(1 through 26) :- '))
    text = input('Enter the text to Encrypt:- ')
    Ciphertext = Encrypt(text, key)
    print(f'CIPHERTEXT: {Ciphertext}')

elif user_input =='d':
    print('Decryption mode selected')
    print()
    key = int(input('Enter the key(1 through 26) :- '))
    text = input('Enter the text to Decrypt:- ')
    Plaintext = Decrypt(text, key)
    print(f'PLAINTEXT: {Plaintext}')



    