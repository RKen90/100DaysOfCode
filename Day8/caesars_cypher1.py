alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l','m','n','o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    new_word = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %=  len(alphabet)
        alphabet[shifted_position]
        new_word += alphabet[shifted_position]
    print(f'Here is the encoded result: {new_word}')
        
        
encrypt("test", 4)
encrypt('z', 9)