def decrypt():
    fileName = input("Please type the name of the file that contains the encrypted text: ")
    File = open(fileName, 'r')
    cipher = File.read()
    num = [1, 2, 3, 4, 5]
    decryption = ' '
    size = len(cipher)
    #Loops through the characters in the word and changed them for encryption
    #LOOP 1
    for x in range(len(cipher)):
        char = cipher[x]
        #This handles all upper case letters
        if(char.isupper()):
            decryption += chr((ord(char) - num[0] - 65) % 26 + 65)
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
            decryption += chr((ord(char) - num[1] - 65) % 26 + 65)
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
            decryption += chr((ord(char) - num[2] - 65) % 26 + 65)
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
            decryption += chr((ord(char) - num[3] - 65) % 26 + 65)
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
            decryption += chr((ord(char) - num[4] - 65) % 26 + 65)
        #This handles all lower case letters
        else:
            decryption += chr((ord(char) - num[4] - 97) % 26 + 97)
    
    print(f"Decrypted String: {decryption}")