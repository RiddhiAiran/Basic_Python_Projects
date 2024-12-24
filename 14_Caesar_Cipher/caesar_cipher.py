import os 
import time

from logo import logo

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def typing(message, delay=0.05):
    """Print a message with a typing effect."""
    for letter in message:
        print(letter, end='', flush=True)
        time.sleep(delay)

def hold_screen(message="Press Enter to continue..."):
    """Hold the screen until the user presses Enter."""
    input(message)


alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caesar():
    clear_screen()
    print(logo)
    typing("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    direction = input().strip().lower()
    if direction not in ['encode', 'decode']:
        typing("Invalid option. Please choose 'encode' or 'decode'.\n")
    else:
        typing("Type your message: ")
        text = input().lower()
        typing("Type the shift number: ")
        shift_amount = int(input())
    output_text = ''
    if direction == 'decode':
        shift_amount *= -1
    for letter in text:
        if letter not in alphabets:
            output_text += letter
        else:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
    typing(f"Here is the {direction} result : {output_text}\n")


# Main program
while True:
    clear_screen()
    typing("Type 'yes' if you want to encode/decode your message. Otherwise type 'no' :")
    status = input().strip().lower()
    if status not in ["y","yes"]:
        typing("Good Bye\n")
        break
    else:
        hold_screen()
        caesar()
        hold_screen()
        
        