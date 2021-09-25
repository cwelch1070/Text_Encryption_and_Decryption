#Function to encrypt word and print to file
def encrypt():
    user1 = input("Enter a line of text to encrypt: ")
    user2 = int(input("Enter the number of shifts needed for this type of encryption: "))
    
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
