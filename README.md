# AJCrypter
 my img-to-pdf-encryption program

Uses TKinter to show a GUI. Allowed file types for conversion are .jpeg/jpg and .pdf.
User selects a file from explorer. If path exists, conversion/encryption begins.

File path is accessed and changed using 'os.path.splitext', which creates an array: [root, extension].
If the extension is .pdf, '_encrypted' is added to the pathname in the SAME ROOT DIRECTORY.
If the extension is an image file, it is converted to pdf (using img2pdf module). Then a new pdf is created where '_encrypted' is added to the path name.

During excryption, the user is prompted to pick a pwd and they must enter the same pwd twice. Program is terminated if the user entry is empty or if they fail to provide identical passwords after 3 attempts.
Once they match, file is encrypted using pikepdf module (and, if original file was an image, the temporary pdf file is now deleted so only the encrypted pdf remains)

Last worked on: Sept 2020
