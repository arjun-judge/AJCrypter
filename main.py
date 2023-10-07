import tkinter
from tkinter import filedialog
import img2pdf
from PIL import Image
import os
import sys
import pyautogui
from pathlib import Path
import pikepdf


def convertImgPdf(img_path, pdf_path):
    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()
    print("Successfully converted " + img_path + " to " + pdf_path)


def get_pwd():
    counter = 1

    pwd1 = pyautogui.prompt('Enter password', title='Enter Password')

    if pwd1 is None:
        print("You exited. Terminating.")
        sys.exit()
    pwd2 = pyautogui.prompt('Confirm password', title='Confirm Password')
    if pwd2 is None:
        print("You exited. Terminating.")
        sys.exit()
    if pwd1 == pwd2:
        return pwd1
    else:
        pwd_same = False

    while not pwd_same:
        counter += 1
        if counter == 4:
            print("Too many tries. Terminating.")
            sys.exit()
        pwd1 = pyautogui.prompt('Your Passwords did not match. Try again:', title='Re-enter Password')
        pwd2 = pyautogui.prompt('Confirm re-entered password', title='Confirm re-entered Password')
        if pwd1 == pwd2:
            return pwd1


def encrypt(tempfile, endfile, num):
    print("Starting encryption of " + tempfile + "...")
    password = get_pwd()
    with pikepdf.open(tempfile) as pdf:
        pdf.save(endfile, encryption=pikepdf.Encryption(user=password, owner=password))
    if num == 0:
        os.remove(tempfile)
    print("Encryption Completed.")
    sys.exit()


root = tkinter.Tk()
root.withdraw()  # use to hide tkinter window
home = str(Path.home())
ftypes = [('jpg/jpeg/pdf files', '*.jpg;*.jpeg;*.pdf'),]
path = filedialog.askopenfilename(parent=root, initialdir=home, title='AJcrypter: Select JPEG/JPG or PDF file.',
                                  filetypes=ftypes)

if len(path) > 0:
    print("File selected: %s" % path)
    split_path = os.path.splitext(path)
    new_ext = ".pdf"
    str_encrypted = "_encrypted"
    new_path = os.path.join(split_path[0] + str_encrypted + new_ext)

    find_ext = os.path.splitext(path)
    if find_ext[1].lower() == ".pdf":
        encrypt(path, new_path, 1)
    else:
        split_path2 = os.path.split(path)
        new_end = "convertPDFtempfile.pdf"
        new_path2 = os.path.join(split_path2[0] + os.path.sep + new_end)
        convertImgPdf(path, new_path2)
        encrypt(new_path2, new_path, 0)
else:
    print("Filedialog closed. Terminating.")
    sys.exit()
