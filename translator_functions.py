import re

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', " ": "/"}


def to_morse():
    message = input("Type in the text you want to translate (only latin alphabet or numbers): \n").upper()
    translated_message = ""
    for letter in message:
        try:
            translated_message += MORSE_CODE_DICT[letter] + " "
        except KeyError:
            print("Seems like you used unsupported characters. Please try again.")
            to_morse()
            return
    print(f'Your message in Morse code is ("/" represents space):\n{translated_message[:-1]}\n')


def from_morse():
    message = input('Type in the Morse code you want to translate (use "/" for space):\n')
    message = re.split(" | / ", message)
    translated_message = []
    for letter in message:
        try:
            translated_message.append(list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(letter)])
        except ValueError:
            print("Seems like you used unsupported characters. Please try again.")
            from_morse()
            return
    translated_message = "".join(translated_message)
    print(f'Your Morse code translates to:\n{translated_message}\n')
