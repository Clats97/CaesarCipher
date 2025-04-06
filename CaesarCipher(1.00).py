import os

RED = "\033[31m"
BLUE = "\033[34m"
BLACK = "\033[30m"
RESET = "\033[0m"

def print_banner():
    banner = RED + r""" ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    
██║     ███████║█████╗  ███████╗███████║██████╔╝    
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    
                                                    
     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗      
    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗     
    ██║     ██║██████╔╝███████║█████╗  ██████╔╝     
    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗     
    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║     
     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    
""" + RESET
    print(banner)
    print(BLUE + "C A E S A R   C I P H E R" + RESET, end="")
    print(" " + RED + "Version 1.00" + RESET)
    print(BLACK + "By Joshua M Clatney - Ethical Pentesting Enthusiast" + RESET)
    print() 

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result.upper()

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print("Select an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("Press Enter to exit")
        option = input("Enter option: ").strip()

        if option == "":
            break
        if option == "1":
            shift_input = input("Enter shift value (number): ").strip()
            try:
                shift = int(shift_input)
            except ValueError:
                input("Invalid shift value. Press Enter to return.")
                continue
            text = input("Enter text to encrypt: ")
            encrypted = caesar_encrypt(text, shift)
            print("\nEncrypted text: " + encrypted)
            input("\nPress Enter to return to the home screen...")

        elif option == "2":
            shift_input = input("Enter shift value (number): ").strip()
            try:
                shift = int(shift_input)
            except ValueError:
                input("Invalid shift value. Press Enter to return.")
                continue
            text = input("Enter text to decrypt: ")
            decrypted = caesar_decrypt(text, shift)
            print("\nDecrypted text: " + decrypted)
            input("\nPress Enter to return to the home screen...")
        else:
            input("Invalid option. Press Enter to try again.")

if __name__ == "__main__":
    main()