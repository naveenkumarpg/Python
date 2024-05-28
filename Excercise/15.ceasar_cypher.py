alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

action_type = str(input('Encode or Decode\n').lower())
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print(text)

def encode(plain_text, shifter) :
    final_string = ''
    
    for letter in plain_text :
        if letter in alphabet :
            index = alphabet.index(letter)      
            encode_index = index + shifter
            if encode_index >= 25 :
                encode_index-= 25
            encoded_letter = alphabet[encode_index]
            final_string+= encoded_letter
        else :
            final_string+= letter
            
    return final_string

def decode(plain_text,shifter) :
    final_string =''    
    for letter in plain_text :
        if letter in alphabet :
            index = alphabet.index(letter)
            decoded_index = index-shifter
            if decoded_index < 0 :
                decoded_index+= 25
            decoded_letter = alphabet[decoded_index]
            final_string += decoded_letter
        else :
            final_string+= letter
    return final_string

if action_type == 'encode' :
    print('Encoding the message ...')
    encoded_string = encode(plain_text = text, shifter=shift)
    print(encoded_string)    
elif (action_type == 'decode') :
    print('Decoding the message ...')
    decoded_string = decode(plain_text = text, shifter=shift)
    print(decoded_string)
else :
    print("No types are matching, you cant continue")

