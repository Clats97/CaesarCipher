import tkinter as tk
from tkinter import messagebox

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
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher GUI 1.00")
        self.geometry("500x600")
        self.frames = {}
        for F in (HomeFrame, EncryptFrame, DecryptFrame):
            frame = F(parent=self, controller=self)
            self.frames[F] = frame
            frame.place(relwidth=1, relheight=1)
        self.show_frame(HomeFrame)
    
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

class HomeFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        ascii_art = (
            " ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗     \n"
            "██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    \n"
            "██║     ███████║█████╗  ███████╗███████║██████╔╝    \n"
            "██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    \n"
            "╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    \n"
            " ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    \n"
            "                                                    \n"
            "     ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗       \n"
            "    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗      \n"
            "    ██║     ██║██████╔╝███████║█████╗  ██████╔╝      \n"
            "    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗      \n"
            "    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║      \n"
            "     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      \n"
        )
        label_art = tk.Label(self, text=ascii_art, fg="red", font=("Courier", 9), justify="left")
        label_art.pack(pady=10)
        
        header_frame = tk.Frame(self)
        header_frame.pack(pady=5)
        label_title = tk.Label(header_frame, text="C A E S A R   C I P H E R", 
                               fg="blue", font=("Courier", 12))
        label_title.pack(side="left", padx=10)
        label_version = tk.Label(header_frame, text="Version 1.00", 
                                 fg="red", font=("Courier", 12))
        label_version.pack(side="left", padx=10)
        
        label_by = tk.Label(self, text="By Joshua M Clatney - Ethical Pentesting Enthusiast", 
                            fg="black", font=("Arial", 10))
        label_by.pack(pady=5)
        
        label_div = tk.Label(self, text="-----------------------------------------------------")
        label_div.pack(pady=5)
        label_options = tk.Label(self, text="Options:", font=("Arial", 12, "bold"))
        label_options.pack(pady=5)
        
        btn_encrypt = tk.Button(self, text="Encrypt Text", width=20,
                                command=lambda: controller.show_frame(EncryptFrame))
        btn_encrypt.pack(pady=5)
        
        btn_decrypt = tk.Button(self, text="Decrypt Text", width=20,
                                command=lambda: controller.show_frame(DecryptFrame))
        btn_decrypt.pack(pady=5)

class EncryptFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Encrypt Text", font=("Arial", 14))
        label.pack(pady=10)
        
        self.text_label = tk.Label(self, text="Enter text to encrypt:")
        self.text_label.pack()
        self.text_input = tk.Text(self, height=5, width=40)
        self.text_input.pack(pady=5)
        
        self.shift_label = tk.Label(self, text="Enter shift value (1-25):")
        self.shift_label.pack()
        self.shift_entry = tk.Entry(self, width=40)
        self.shift_entry.pack(pady=5)
        
        btn_process = tk.Button(self, text="Encrypt", command=self.process_encrypt)
        btn_process.pack(pady=10)
        
        self.result_label = tk.Label(self, text="Encrypted text:", font=("Arial", 12))
        self.result_label.pack()
        self.result_output = tk.Text(self, height=5, width=40, state="disabled")
        self.result_output.pack(pady=5)
        
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)
    
    def process_encrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        shift_input = self.shift_entry.get().strip()
        
        if not text or not any(c.isalpha() for c in text):
            messagebox.showerror("Input Error", "Text must contain at least one alphabetic character.")
            return
        try:
            shift = int(shift_input)
        except ValueError:
            messagebox.showerror("Input Error", "Shift value must be an integer.")
            return
        
        result = caesar_encrypt(text, shift)
        self.result_output.config(state="normal")
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, result)
        self.result_output.config(state="disabled")

class DecryptFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        label = tk.Label(self, text="Decrypt Text", font=("Arial", 14))
        label.pack(pady=10)
        
        self.text_label = tk.Label(self, text="Enter text to decrypt:")
        self.text_label.pack()
        self.text_input = tk.Text(self, height=5, width=40)
        self.text_input.pack(pady=5)
        
        self.shift_label = tk.Label(self, text="Enter shift value (number):")
        self.shift_label.pack()
        self.shift_entry = tk.Entry(self, width=40)
        self.shift_entry.pack(pady=5)
        
        btn_process = tk.Button(self, text="Decrypt", command=self.process_decrypt)
        btn_process.pack(pady=10)
        
        self.result_label = tk.Label(self, text="Decrypted text:", font=("Arial", 12))
        self.result_label.pack()
        self.result_output = tk.Text(self, height=5, width=40, state="disabled")
        self.result_output.pack(pady=5)
        
        btn_home = tk.Button(self, text="Return Home", command=lambda: controller.show_frame(HomeFrame))
        btn_home.pack(pady=10)
    
    def process_decrypt(self):
        text = self.text_input.get("1.0", tk.END).strip()
        shift_input = self.shift_entry.get().strip()
        
        if not text or not any(c.isalpha() for c in text):
            messagebox.showerror("Input Error", "Text must contain at least one alphabetic character.")
            return
        try:
            shift = int(shift_input)
        except ValueError:
            messagebox.showerror("Input Error", "Shift value must be an integer.")
            return
        
        result = caesar_decrypt(text, shift)
        self.result_output.config(state="normal")
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, result)
        self.result_output.config(state="disabled")

if __name__ == "__main__":
    app = Application()
    app.mainloop()