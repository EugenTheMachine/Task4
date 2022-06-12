# declaring the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# declaring the message and the key, converting them to the lower register
# and declaring their lengths
inp_mess = input("Введите сообщение для шифрования: ")
message = inp_mess.lower()
mess_len = len(message)
message.lower()
inp_key = input("Введите сообщение-ключ из буквенных символов: ")
key_len = len(inp_key)

# checking whether the key is of correct symbol-form
cp = 0
for i in range(key_len):
    if alphabet.find(inp_key[i]) < 0:
        print("Ключ содержит запрещенные символы. Работа программы приостановлена.")
        cp += 1
        break
# if the key is correct, we can move on
if cp == 0:
    key = inp_key.lower()

    # initializing the "Vigenere"-message string
    vigenere_message = '0'

    # making the key-length equal to the message-length
    if key_len < mess_len:
        for i in range(mess_len - key_len):
            key += key[i]

    # declaring the d[elta] variable for correct work of the key
    d = 0

    # converting the entered message into the Vigenere-type message using the entered key
    # and ignoring the symbols that are not included in the alphabet
    for i in range(mess_len):
        m = i - d
        if alphabet.find(message[i]) >= 0:
            mess_chr = ord(message[i]) - 97
            key_chr = ord(key[m]) - 97
            vigenere_chr = chr((mess_chr + key_chr) % 26 + 97)
            if inp_mess[i].isupper():
                vigenere_message += vigenere_chr.upper()
            else:
                vigenere_message += vigenere_chr
        else:
            vigenere_message += message[i]
            d += 1

    # printing the completed Vigenere-type message
    print(vigenere_message.replace(vigenere_message[0], ''))
