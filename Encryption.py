#Function to encrypt word and print to file
def encrypt():
    #The encryption is stored in the cipher variable
    cipher = ' '
    size = len(user1)
    #Loops through the characters in the word and changed them for encryption
    for x in range(len(user1)):
        char = user1[x]
        #This handles all upper case letters
        if(char.isupper()):
            cipher += chr((ord(char) + user2 - 65) % 26 + 65)
        #This handles all lower case letters
        else:
            cipher += chr((ord(char) + user2 - 97) % 26 + 97)
    
    print(f"Encrypted String: {cipher}")
    
    #Prints encryption of word to file
    sample = open('Crypto.txt', 'w')
    print(cipher, file = sample)
    sample.close()
    
    return cipher

def decrypt():
    cipher = encrypt()
    num = [1, 2, 3, 4, 5]
    decryption = ' '
    size = len(cipher)
    #Loops through the characters in the word and changed them for encryption
    #LOOP 1
    for x in range(len(cipher)):
        char = cipher[x]
        #This handles all upper case letters
        if(char.isupper()):
            decryption += chr((ord(char) - num[0])) #- 65) % 26 + 65)
        #This handles all lower case letters
        else:
            decryption += chr((ord(char) - num[0] - 97) % 26 + 97)
            
    print(f"Decrypted String: {decryption}")
    decryption = ' '
            
    #LOOP 2
    for x in range(len(cipher)):
        char = cipher[x]
        #This handles all upper case letters
        if(char.isupper()):
            decryption += chr((ord(char) - num[1])) #- 65) % 26 + 65)
        #This handles all lower case letters
        else:
            decryption += chr((ord(char) - num[1] - 97) % 26 + 97)
            
    print(f"Decrypted String: {decryption}")
    decryption = ' '
       
    #LOOP 3
    for x in range(len(cipher)):
        char = cipher[x]
        #This handles all upper case letters
        if(char.isupper()):
            decryption += chr((ord(char) - num[2])) #- 65) % 26 + 65)
        #This handles all lower case letters
        else:
            decryption += chr((ord(char) - num[2] - 97) % 26 + 97)
            
    print(f"Decrypted String: {decryption}")
    decryption = ' '
          
    #LOOP 4       
    for x in range(len(cipher)):
        char = cipher[x]
        #This handles all upper case letters
        if(char.isupper()):
            decryption += chr((ord(char) - num[3])) #- 65) % 26 + 65)
        #This handles all lower case letters
        else:
            decryption += chr((ord(char) - num[3] - 97) % 26 + 97)
    
    print(f"Decrypted String: {decryption}")
    decryption = ' '   
         
    #LOOP 5
    for x in range(len(cipher)):
        char = cipher[x]
        #This handles all upper case letters
        if(char.isupper()):
            decryption += chr((ord(char) - num[4])) #- 65) % 26 + 65)
        #This handles all lower case letters
        else:
            decryption += chr((ord(char) - num[4] - 97) % 26 + 97)
    
    print(f"Decrypted String: {decryption}")
    
#Gets user input for stirng to encrypt and how far to shift 
user1 = input("Enter a line of text to encrypt: ")
user2 = int(input("Enter the number of shifts needed for this type of encryption: "))

#Function call
encrypt()
decrypt()