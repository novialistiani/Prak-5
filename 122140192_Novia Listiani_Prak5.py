#Novia Listiani
#122140192
#PBO RB

#program ini adalah game sederhana yang meminta user untuk menebak angka 1-100
#user diminta untuk memasukkan angka tebakannya
#program akan memberikan petunjuk apakah tebakan pengguna terlalu kecil, terlalu besar, atau benar.
#program ini menggunakan library tkinter
 
import tkinter as tk
from tkinter import messagebox
import random

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Tebak Angka")
        self.master.geometry("300x150")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(master, text="Tebak angka antara 1 dan 100:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.button = tk.Button(master, text="Tebak", command=self.check_guess)
        self.button.pack()
        
    def check_guess(self):
        self.attempts += 1
        guess = int(self.entry.get())
        
        if guess < self.secret_number:
            messagebox.showinfo("Hasil", "Angka terlalu kecil!")
        elif guess > self.secret_number:
            messagebox.showinfo("Hasil", "Angka terlalu besar!")
        else:
            messagebox.showinfo("Hasil", f"Selamat! Anda berhasil menebak angka {self.secret_number} dalam {self.attempts} percobaan.")
            self.master.destroy()

def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
