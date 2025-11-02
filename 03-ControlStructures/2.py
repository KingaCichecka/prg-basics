###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char:  
        
        if char:
            encrypted_char = chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        
        else:
            encrypted_char = chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
    else:
        encrypted_char = char  
    
    encrypted_text += encrypted_char

print("Original text:", plain_text)
print("Encrypted text:", encrypted_text)
