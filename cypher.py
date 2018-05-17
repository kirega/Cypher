"""
Joseph Mutiga Kirega
P15/1567/2015
Cryptography- Assingment 2 
"""

plaintext = "Once upon a time in a land"

#Convert each letter in the plaintext to ascii equivalent string.
def cypher(plaintext):
    cyphertext = [ord(char) for char in plaintext]
    return cyphertext
    
#decipher the encrypted text back to plaintext
def decypher(cyphertext):
    plaintext = [chr(char) for char in cyphertext]
    return ''.join(plaintext)
def convert_to_string(x):
    return str(x)

print(''.join(map(convert_to_string, cypher(plaintext))))
print(decypher(cypher(plaintext)))