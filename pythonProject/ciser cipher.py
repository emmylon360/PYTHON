alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'o','p','q','r','s','t','u','v','w','x','y','z']
direction= input('type encode to encrypt, type decode to decrypt\n').lower()
text = input('type your message\n').lower()
shift = int(input('type your shift number: \n'))

def encrypt(plain_text,shift_position):
     cipher_text =''
     for letter in plain_text:
         position = alphabets.index(letter)
         new_position = position + shift_position
         new_letter = alphabets[new_position]
         cipher_text += new_letter
     print(f'the encoded text is {cipher_text}')
encrypt(plain_text=text,shift_position=shift)


# def decrypt(coded_text,shift_position):
#     formed_text = ''
#     for letter in coded_text:
#         position = alphabets.index(letter)
#         new_position = position - shift_position
#         new_letter = alphabets[new_position]
#         formed_text += new_letter
#     print(f'the decoded text is {formed_text}')
#
# decrypt(coded_text=text, shift_position=shift)


