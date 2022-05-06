from os import system
from tkinter import *
from tkinter import ttk
import platform
import subprocess
import re


window = Tk()
window.geometry("500x500")
window.title("ISOChecker")
style = ttk.Style()
header = ttk.Label(text="ISOChecker", font=("Helvetica", 16))

def switch_to_sha256():
    def check_sha256():
        str = ""
        if platform.system() == 'Windows':
            check = subprocess.run(["certutil", "-hashfile", sha256_input_iso_entry.get(), "sha256"], capture_output=True, text=True)
            x = check.stdout.split("\n")
            del x[0]
            x.remove("CertUtil: -hashfile command completed successfully.")
            y = str.join(x)
            print(x)
            if y == sha256_input_hash_entry.get():
                sha256sum.destroy()
                goodfile = Tk()
                goodfile.geometry("500x500")
                goodfile.title("ISOChecker")
                checks = ttk.Label(text="Good file!", font=("Helvetica", 12))
                checks.pack()
                goodfile.mainloop()
            else:
                sha256sum.destroy()
                badfile = Tk()
                badfile.geometry("500x500")
                badfile.title("ISOChecker")
                checks = ttk.Label(text="Bad file! Do not use!", font=("Helvetica", 12))
                checks.pack()
                badfile.mainloop()
            
        elif platform.system() == 'Darwin':
            check = subprocess.run(["shasum", "-a", "256", sha256_input_iso_entry.get()], capture_output=True, text=True)
            x = check.stdout
            if x == sha256_input_hash_entry.get():
                sha256sum.destroy()
                goodfile = Tk()
                goodfile.geometry("500x500")
                goodfile.title("ISOChecker")
                checks = ttk.Label(text="Good file!", font=("Helvetica", 12))
                checks.pack()
                goodfile.mainloop()
            else:
                sha256sum.destroy()
                badfile = Tk()
                badfile.geometry("500x500")
                badfile.title("ISOChecker")
                checks = ttk.Label(text="Bad file! Do not use!", font=("Helvetica", 12))
                checks.pack()
                badfile.mainloop()
        elif platform.system() == "Linux":
            check = subprocess.run(["sha256sum", sha256_input_iso_entry.get()], capture_output=True, text=True)
            y = check.stdout.split(' ', 1)[0]
            if y == sha256_input_hash_entry.get():
                sha256sum.destroy()
                goodfile = Tk()
                goodfile.geometry("500x500")
                goodfile.title("ISOChecker")
                checks = ttk.Label(text="Good file!", font=("Helvetica", 12))
                checks.pack()
                goodfile.mainloop()
            else:
                sha256sum.destroy()
                badfile = Tk()
                badfile.geometry("500x500")
                badfile.title("ISOChecker")
                checks = ttk.Label(text="Bad file! Do not use!", font=("Helvetica", 12))
                checks.pack()
                badfile.mainloop()


    window.destroy()
    sha256sum = Tk()
    sha256sum.geometry("500x500")
    sha256sum.title("ISOChecker")
    sha256_input_label_iso = ttk.Label(text="Input your ISO file path (full), (please remove quotation marks)", font=("Helvetica", 12))
    sha256_input_iso_entry = ttk.Entry(sha256sum, width=50)
    sha256_input_label_hash = ttk.Label(text="Input your good SHA256SUM hash data (copy and paste)", font=("Helvetica", 12))
    sha256_input_hash_entry = ttk.Entry(sha256sum, width=50)
    sha256_checksum = ttk.Button(text="Check", command=check_sha256)

    sha256_input_label_iso.pack()
    sha256_input_iso_entry.pack()
    sha256_input_label_hash.pack()
    sha256_input_hash_entry.pack()
    sha256_checksum.pack()
    sha256sum.mainloop()

def switch_to_gpg_screen():
    def gpg_checksum():
        gpg.destroy()
        gpgsum = Tk()
        gpgsum.geometry("500x500")
        gpgsum.title("ISOChecker")
    window.destroy()
    gpg = Tk()
    gpg.geometry("500x500")
    gpg.title("ISOChecker")
    notice = ttk.Label(text="PLEASE NOTE: Please import your keys before you run this.", font=("Helvetica", 12))
    notice1 = ttk.Label(text="This is because of the complexity and the different methods of importing public keys")
    notice2 = ttk.Label(text="I am only one person, and I am still a student, so we will have to live with this limitation.")
    notice3 = ttk.Label(text="Also, this may seem obvious, but, PLEASE MAKE SURE GPG IS INSTALLED.")
    notice4 = ttk.Label(text="THIS WILL NOT WORK WITHOUT GPG INSTALLED.")
    understand = ttk.Button(text="I understand", command=gpg_checksum)
    notice.pack()
    notice1.pack()
    notice2.pack()
    notice3.pack()
    notice4.pack()
    understand.pack()
    gpg.mainloop()

SHA256SUMSELECTOR = ttk.Button(text="SHA256SUM", command=switch_to_sha256)
GPGSELECTOR = ttk.Button(text="GPG", command=switch_to_gpg_screen)

header.pack()
SHA256SUMSELECTOR.pack()
GPGSELECTOR.pack()
window.mainloop()
