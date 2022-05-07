# ISOChecker
It is a GUI ISO checker, which is made in python with Tkinter, and can process SHA256 and GPG Checksums.

#### Are you a sysadmin who is tired of verifying their ISO's? Are you a server architect who just has to manage all those services? Don't worry!
The ISOChecker is a GUI program that allows you to simply input to values, and get a response of "Good File!", or "Bad File!".

Of course, with the actual tools themselves, they have a lot of subfeatures, that go deeper than what this program covers, but that is the point.

## This is supposed to be simple!

I made this as a little project.

The actual python file can be run on any OS, but there have only been built binaries for Windows and Linux.

I hope you find this useful

Kind Regards,
Alphons

# Documentation
Running the program will give you, as of now, two options:
SHA256 and GPG

These two options are what you get to verify your ISO.
I would recommend GPG, as the hash can only be generated by the actual author.

## SHA256
There will be two entry boxes,
One for your ISO directory, and one for your Hash.

If your ISO file is not in the same directory as the tool, you must put in the full path.
**You must also remove quotation marks, as it is currently a limitation for it to work.**

Clicking the "Check" button will give you either one of two windows.
There will either be one that says "Good file!"
Or there will be one that says "Bad File! Do Not Use!"

## GPG
A current limitation with GPG is that if you require to have public keys beforehand, you must use the GPG commandline tool to import the signature from the ISO Distributor beforehand.

This is because of the complex ways that GPG can import keys.

There will be a warning text box with basically this text from above, and there will a button that says "I Understand"

Then there will be two entry boxes.
There will be one for your ISO file, and there will be one for your signature file.
This signature file will be a .sig or .asc file.

**Please remember to remove the quotation marks from the path before clicking the check button.**

When you click the "Check Button", it will give you either of two windows.

If it is a Good Signature, you will get "Good File!"

If it is a Bad Signature, you will get "Bad File! Do Not Use!"

# Licensing
This is licensed under the MIT license

# Credit
This was built with the packages OS, Tkinter, Platform, Subprocess, and Regex

Binaries built with PyInstaller on Windows and WSL.
