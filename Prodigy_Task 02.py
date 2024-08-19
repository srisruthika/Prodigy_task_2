from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image
import numpy as np

class ImageEncryptionTool:
    def __init__(self, master):
        self.master = master
        master.title("Image Encryption Tool")

        self.label = Label(master, text="Choose an option to encrypt or decrypt an image")
        self.label.pack()

        self.encrypt_button = Button(master, text="Encrypt", command=self.encrypt_image)
        self.encrypt_button.pack()

        self.decrypt_button = Button(master, text="Decrypt", command=self.decrypt_image)
        self.decrypt_button.pack()

    def encrypt_image(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return

        try:
            image = Image.open(filepath)
            encrypted_image = self.apply_pixel_manipulation(image, "encrypt")
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                encrypted_image.save(save_path)
                messagebox.showinfo("Success", "Image encrypted and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decrypt_image(self):
        filepath = filedialog.askopenfilename()
        if not filepath:
            return

        try:
            image = Image.open(filepath)
            decrypted_image = self.apply_pixel_manipulation(image, "decrypt")
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            if save_path:
                decrypted_image.save(save_path)
                messagebox.showinfo("Success", "Image decrypted and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def apply_pixel_manipulation(self, image, operation):
        pixel_data = np.array(image)
        if operation == "encrypt":
            manipulated_data = (pixel_data + 100) % 256
        elif operation == "decrypt":
            manipulated_data = (pixel_data - 100) % 256
        else:
            raise ValueError("Invalid operation")

        return Image.fromarray(manipulated_data.astype(np.uint8))

def main():
    root = Tk()
    app = ImageEncryptionTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()
