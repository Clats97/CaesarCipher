# CaesarCipher
A simple Caesar cipher script that can encrypt plaintext by selecting a shift. The reverse is done to decrypt. Very simple to use.

# Caesar Cipher Script

## Features

- **Colorful ASCII Art Banner:**  
  Displays a red ASCII art logo, the title "C A E S A R   C I P H E R" in blue, version information in red, and credits in black.
  
- **Encryption & Decryption Options:**  
  - **Encrypt:** Shift the letters of your input text by a specified value.
  - **Decrypt:** Reverse the encryption by applying the inverse shift.
  
- **Uppercase Output:**  
  All output (encrypted or decrypted) is converted to uppercase.

- **User-Friendly Navigation:**  
  After each operation, the user can press Enter to return to the home screen. Pressing Enter at the home screen exits the script.

## Requirements

- **Python 3.x**  
  Ensure Python 3 is installed on your system. You can verify your Python version by running:
 
  python3 --version
  

- **ANSI-Compatible Terminal:**  
  The script uses ANSI escape codes to display colored text. Make sure your terminal supports these codes.  

## Installation

1. **Clone or Download the Repository:**  
   Save the script file in a directory of your choice.

2. **Verify Python Installation:**  
   Confirm that Python 3 is installed on your system.

## Usage

1. Git clone or download the repository. 

2. Run the script.

3. Follow the on screen prompts to use it.
  

4. **Follow the On-Screen Prompts:**
   - **Option 1 (Encrypt):** Enter a shift value and the text you want to encrypt.
   - **Option 2 (Decrypt):** Enter a shift value and the text you want to decrypt.
   - **Exit:** Press Enter on the home screen to exit the script.

## Code Structure

- **print_banner():**  
  Displays the ASCII art banner along with colored title, version, and credit information.

- **caesar_encrypt(text, shift):**  
  Encrypts the provided text by shifting each alphabetical character by the specified amount, and returns the result in uppercase.

- **caesar_decrypt(text, shift):**  
  Decrypts the text by applying the negative of the provided shift value. This function uses the `caesar_encrypt` function internally.

- **main():**  
  Contains the main loop that manages user interactions and the menu options.

## License

Distributed under the Apache 2.0 License. 

## Feedback & Contributions

If you have suggestions, feedback, or improvements, please open an issue or submit a pull request.

**Author**
Joshua M Clatney (Clats97)
Ethical Pentesting Enthusiast

Copyright 2025 Joshua M Clatney (Clats97)

---
