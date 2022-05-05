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
            x.remove("SHA256 hash of C:\\Users\\helpm\\Desktop\\Computer Stuff\\Computer nerd\\ISO's\\alpine-standard-3.15.4-x86_64.iso:")
            x.remove("CertUtil: -hashfile command completed successfully.")
            y = str.join(x)
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
            print(check.stdout)

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

SHA256SUMSELECTOR = ttk.Button(text="SHA256SUM", command=switch_to_sha256)

header.pack()
SHA256SUMSELECTOR.pack()
window.mainloop()
