###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if encrypted_text:
         encrypted_char = chr(ord(char) + 1)

    
new = encrypted_text + encrypted_char
print(f"{plain_text}")
print(f"{new}")