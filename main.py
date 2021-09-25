import Encryption
import Decryption

#Main    
#Function call
print("Type encrypt or decrypt below")
choice = input("Would you like to encrypt or decrypt text?")

if(choice == 'encrypt'):
    Encryption.encrypt()
else:
    Decryption.decrypt()