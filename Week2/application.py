import LSB as lsb
import AES as Cipher
import os

# from the tkinter library
from tkinter import *
  
# import filedialog module
from tkinter import filedialog

class GUI: 
    
    def __init__(self,master):
        master.title("Steganography")
    
        #Create a fullscreen window
        # master.state("zoomed")

        # Set window title
        master.title('File Explorer')

        master.geometry("500x500")

        #Set window background color
        master.config(background = "white")
        
                
        # Create a File Explorer label
        self.label_file_explorer = Label(master,
                                    text = "File Explorer using Tkinter",
                                    width = 100, height = 4,
                                    fg = "blue").pack(pady = 10)
        
        self.new_window_explore = Button(master,
                                text = "Embeding your secret text",
                                command =lambda: self.openEmbeddingWindow()).pack(pady = 10)
        
        self.extracting_new_window = Button(master,
                            text = "Extracting your stego image",
                            command =lambda: self.openExtractingWindow()).pack(pady = 10)

        # self.button_exit = Button(master,
        #                     text = "Exit",
        #                     command = exit).pack(pady = 10)
        
    def browseFiles(self):
            self.coverImagePath = filedialog.askopenfilename(initialdir = "/",
                                            title = "Select a File",
                                            filetypes = (('image files', '.png'),
                                                          ('image files', '.jpg'),
                                                        ("all files",
                                                            "*.*")))
            self.lCoverImage.config(text="File Opened: "+ self.coverImagePath)
            
    def browseFolder(self):
        self.stegoImagePath = filedialog.askdirectory() 
        self.lStegoImagePath.config(text="Folder Opened: "+ self.stegoImagePath)
        
    def extBrowseFiles(self):
        self.extStegoImagePath = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (('image files', '.png'),
                                                        ('image files', '.jpg'),
                                                    ("all files",
                                                        "*.*")))
        self.lExtStegoImagePath.config(text="File Opened: "+ self.extStegoImagePath)
            
    def extBrowseFolder(self):
        self.extPlsDir = filedialog.askdirectory() 
        self.lExtPlsImagePath.config(text="Folder Opened: "+ self.extPlsDir)
    
    def embedding(self, coverImagePath, stegoImagePath, secretMessage, passwordText, plsPasswordText):
        encodedMessage = Cipher.encrypt(secretMessage, passwordText)
        print(encodedMessage)
        lsb.LsbEncoding(coverImagePath, stegoImagePath, encodedMessage, plsPasswordText)
           
    def extracting(self, stegoImagePath, plsDir, plspassword):
        self.decodedText = lsb.LsbDecoding(stegoImagePath, plsDir, plspassword)
        self.finalMessage = Cipher.decrypt(self.decodedText, plspassword)      
        print("Final message :", self.finalMessage)  
        self.lExtfinalMessage.config(text="Final message: "+ self.finalMessage)
        
    def openExtractingWindow(self):
        self.extWindow = Toplevel(window)
        self.extWindow.title("Extracting")
        self.extWindow.geometry("500x500")
        self.extWindow.grab_set()
        self.lTitle = Label(self.extWindow,
            text ="Extracting your stego image").pack(pady = 10)
        
        # Stego Image
        self.lExtChoose = Label(self.extWindow,
            text ="Choose your cover image").pack(pady = 10)
        
        self.lExtStegoImagePath = Label(self.extWindow,
            text ="File Opened ... ")
        self.lExtStegoImagePath.pack(pady = 10)
        self.btnExtBrowseFile = Button(self.extWindow,
                            text = "Browse Files",
                            command =lambda: self.extBrowseFiles())
        self.btnExtBrowseFile.pack(pady = 10)
        
        # Pls password
        self.lExtPassword = Label(self.extWindow,
            text ="Enter your password")
        self.lExtPassword.pack(pady = 10)
        self.txtExtPassword = Text(self.extWindow, height = 1, width = 52)
        self.txtExtPassword.pack(pady = 10)
        
        # Pls dir
        self.lExtStegoImage = Label(self.extWindow,
            text ="Choose your output image").pack(pady = 10)
        
        self.lExtPlsImagePath = Label(self.extWindow,
            text ="File Opened ... ")
        self.lExtPlsImagePath.pack(pady = 10)
        self.btnExtBrowseFile2 = Button(self.extWindow,
                            text = "Browse Folder",
                            command =lambda: self.extBrowseFolder())
        self.btnExtBrowseFile2.pack(pady = 10)
        
        
        # EXTRACTING BUTTON
        self.btnExtracting = Button(
            self.extWindow,
            text="EXTRACTING",
            command=lambda: self.extracting(
                self.extStegoImagePath, 
                self.extPlsDir,
                self.txtExtPassword.get(1.0, "end-1c"))
        ).pack(pady = 10)
        
        self.lExtfinalMessage = Label(self.extWindow,
            text ="Final message: ...")
        self.lExtfinalMessage.pack(pady = 10)
        
        
    def openEmbeddingWindow(self):
        self.embWindow = Toplevel(window)
        self.embWindow.title("Embedding")
        self.embWindow.geometry("500x500")
        self.embWindow.grab_set()
        self.lTitle = Label(self.embWindow,
            text ="Embedding your secret").pack(pady = 10)
        
        # Cover Image
        self.lChoose = Label(self.embWindow,
            text ="Choose your cover image").pack(pady = 10)
        
        self.lCoverImage = Label(self.embWindow,
            text ="File Opened ... ")
        self.lCoverImage.pack(pady = 10)
        self.btnBrowseFile = Button(self.embWindow,
                            text = "Browse Files",
                            command =lambda: self.browseFiles())
        self.btnBrowseFile.pack(pady = 10)
        

        # Secret Text
        self.lSecretText = Label(self.embWindow,
            text ="Enter your secret text")
        self.lSecretText.pack(pady = 10)
        self.txtSecret = Text(self.embWindow, height = 1, width = 52)
        self.txtSecret.pack(pady = 10)

        # Password
        self.lPassword = Label(self.embWindow,
            text ="Enter your password")
        self.lPassword.pack(pady = 10)
        self.txtPassword = Text(self.embWindow, height = 1, width = 52)
        self.txtPassword.pack(pady = 10)
        
        # Stego Image
        self.lStegoImage = Label(self.embWindow,
            text ="Choose your output image").pack(pady = 10)
        
        self.lStegoImagePath = Label(self.embWindow,
            text ="File Opened ... ")
        self.lStegoImagePath.pack(pady = 10)
        self.btnBrowseFile2 = Button(self.embWindow,
                            text = "Browse Folder",
                            command =lambda: self.browseFolder())
        self.btnBrowseFile2.pack(pady = 10)
        
        # EMBEDDING BUTTON
        self.btnEmbedding = Button(
            self.embWindow,
            text="EMBEDDING",
            command=lambda: self.embedding(
                self.coverImagePath, 
                self.stegoImagePath,
                self.txtSecret.get(1.0, "end-1c"), 
                self.txtPassword.get(1.0, "end-1c"), 
                self.txtPassword.get(1.0, "end-1c"))
        ).pack(pady = 10)
        
        # self.button_close = Button(
        #     self.newWindow,
        #     text="Close window",
        #     command=self.newWindow.destroy
        # ).pack(pady = 10)
        
                                                                                                 
# Create the root window
window = Tk()
b=GUI(window) 
# Let the window wait for any events
window.mainloop()