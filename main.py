from simple_term_menu import TerminalMenu
from translator_functions import to_morse, from_morse

# Configure main.py to emulate terminal in output console to show terminal menu properly

# Terminal menu action codes
TRANSLATE_TEXT_TO_MORSE_CODE = 0
TRANSLATE_MORSE_CODE_TO_TEXT = 1
EXIT = 2

print("\033[1mWelcome to Morse code translator\033[0m\n")
while True:
    terminal_menu = TerminalMenu(["Translate text to morse code", "Translate morse code to text", "Exit"])
    selected_action = terminal_menu.show()

    if selected_action == TRANSLATE_TEXT_TO_MORSE_CODE:
        to_morse()
    elif selected_action == TRANSLATE_MORSE_CODE_TO_TEXT:
        from_morse()
    elif selected_action == EXIT:
        print("\033[1mGoodbye\033[0m")
        quit()
