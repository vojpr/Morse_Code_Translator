import re

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', " ": "/"}


def translation():
    def to_morse():
        message = input("Write what you want to translate (only latin alphabet or numbers):\n").upper()

        translated_message = ""
        for each in message:
            try:
                translated_message += MORSE_CODE_DICT[each] + " "
            except KeyError:
                print("Seems like you used unsupported characters. Please try again.")
                to_morse()
                return
        print(f'Your message in Morse code is (" / " represents space):\n{translated_message[:-1]}')

    def from_morse():
        message = input('type in your Morse code (use " / " for space):\n')
        message = re.split(" | / ", message)

        translated_message = []
        for each in message:
            try:
                translated_message.append(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(each)])
            except ValueError:
                print("Seems like you misspelled the code. Please try again.")
                from_morse()
                return
        translated_message = "".join(translated_message)
        print(f'Your Morse code translates to:\n{translated_message}')

    which_way = input('For translation TO Morse code type "1", for translation FROM Morse type "2":\n')
    if which_way == "1":
        to_morse()
    elif which_way == "2":
        from_morse()
    else:
        print('Please type only "1" or "2".')
        translation()


translation()
