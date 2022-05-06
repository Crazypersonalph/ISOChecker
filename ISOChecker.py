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

def switch_to_gpg():
    window.destroy()
    gpgsum = Tk()
    gpgsum.geometry("500x500")
    gpgsum.title("ISOChecker")
    notice = ttk.Label(text="PLEASE NOTE: Please import your keys before you run this. It is because of the complexity of handling gpg public keys, and since I am only one person, you will have to import your public keys beforehand. You can get instructions for importing your public key from your OS distibutor.", font=("Helvetica", 12))
    gpgsum.mainloop()

SHA256SUMSELECTOR = ttk.Button(text="SHA256SUM", command=switch_to_sha256)
GPGSELECTOR = ttk.Button(text="GPG", command=switch_to_gpg)

header.pack()
SHA256SUMSELECTOR.pack()
GPGSELECTOR.pack()
window.mainloop()
