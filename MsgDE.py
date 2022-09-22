

#each character in the substitution
alphabet= "abcdefghijklmnopqrstuvwxyz"
key="qwertyuiopasdfghjklzxcvbnm"

#FunctiondecryptMessage
def decryptMessage (ciphertext, key) :
    # Create a placeholder variable to store the decrvoted plaintext
    plaintext=""
    # Iterate through each character in the decrypted message
    for char in ciphertext:
        index = key. find (char)
        # If the character is in the alphabet
        # replace the character in the key with the corresponding
        # character in the alphabet and add it to the ciphertext
        if (index > -1):
            plaintext += alphabet[index]
        
        else:
            plaintext += char
    
    return plaintext

def encryptMessage (plaintext, key) :
    # Create a placeholder variable to store the ciphertext
    ciphertext=""
    #convert message to Lower case
    plaintext = plaintext.lower();
    # Iterate through each character in the plaintext message
    for char in plaintext:
        index = alphabet.find (char)
        # If the character is in the alphabet replace the character in the alphabet with the corresponding character in the key and add it to the ciphertext.
        if (index > -1):
            ciphertext += key[index]
    
        else:
            ciphertext += char
    
    return ciphertext

#Get input message from the user
message = input("Type a message to encrypt:")
#Encrypt the message
encrypted = encryptMessage (message, key)
# Decrypt the message
decrypted = decryptMessage (encrypted, key)
# Print the original message, the encrypted message,and the decrypted message.
print ("Plaintext message:"+ message)
print ( "Encrypted message:"+ encrypted)
print ( "Decrypted message:"+decrypted)