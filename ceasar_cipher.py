def encrypt(text,shift_key):
  result = ''
  # run through the plain text
  for i in range(len(text)):
    char = text[i]
    # Encrypt uppercase characters (using ASCII)
    if (char.isupper()):
        result += chr((ord(char) + shift_key-65) % 26 + 65)
    # Encrypt lowercase characters (using ASCII)
    else:
        result += chr((ord(char) + shift_key - 97) % 26 + 97)
    return result

message = "Demonstrating ceasar cipher "
shift_key = 7

print ('Message : ' + message)
print ('Shift key : ' + str(shift_key))
print ('Cipher  Equivalent : ' + encrypt(message,shift_key))