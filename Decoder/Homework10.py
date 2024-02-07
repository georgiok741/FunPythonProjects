# Welcome to "Programers_Are_Better_Than_Everyone_2.0 #
#This program allows you to send, recieve, and decode decyphered messages programmer!


#CODE A MESSAGE!"
def code_message(offset):
    #Get Message and Offset
    message = input("Please enter message you don't want normal human beings to understand: ")
    message = message.lower()

    #Fix offset if greater than 26
    if offset > 26:
        offset = offset % 26
    
    #Offset letters by specified amount
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    symbols = """!-,.?' :"""
    new_message = ""
    for i in message:
        if i in symbols:
            index_ = symbols.find(i)
            new_message = new_message + symbols[index_]
        else:
            index_ = alphabet.find(i) - offset
            new_message = new_message + alphabet[index_]        
    print(new_message)

#DECODE A MESSAGE!"
    
def decode_message(offset):
    #Enter recieved message and offset
    message = input("Please enter encrypted message only the best humans can understand: ")

    #Offset back to normal alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    symbols = """!-,.?' :"""
    new_message = ""
    for i in message:
        if i in symbols:
            index_ = symbols.find(i)
            new_message = new_message + symbols[index_]
        else:
            index_ = alphabet.find(i) + offset
            if index_ < 26:
                new_message = new_message + alphabet[index_]
            else:
                index_ = index_ % 26
                new_message = new_message + alphabet[index_]
    print(new_message)

application = int(input("Enter 1 if you would like to encode a message. Enter 2 if you would like to decode a message: "))

if application == 1:
    key = int(input("Enter a numerical key to encrypt your message: "))
    code_message(key)
elif application == 2:
    key = int(input("Enter a numerical key to decrypt your message: "))
    decode_message(key)
else:
    print("Invalid Input!")
