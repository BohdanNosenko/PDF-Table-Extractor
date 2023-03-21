import customtkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tabula import read_pdf
import pandas as pd

class App(customtkinter.CTk):

    filename = None

    def __init__(self):
        super().__init__()

        self.title("PDF2EXCEL")
        self.geometry("300x300")

        self.button1 = customtkinter.CTkButton(master=self, text="Select PDF File", command=self.button_function)
        self.button1.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        self.button2 = customtkinter.CTkButton(master=self, text="Convert", command=self.convert, state='normal')
        self.button2.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)



    def button_function(self):
        global filename
        filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
        filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
        if filename == '':
            pass
        else:
            showinfo(title='Selected File', message=filename)

    def convert(self):
        global filename

        df = read_pdf(filename, pages="all")
        new_filename = filename.replace("pdf", "xlsx")

        if len(df) > 1:
            with pd.ExcelWriter(new_filename) as writer:
                for i in range(len(df)):
                    df[i].to_excel(writer, sheet_name=f'Sheet{i}')
        else:
            try:
                df[0].to_excel(new_filename)
            except IndexError:
                showinfo(title='Selected File', message='No tables found in this document.')

        showinfo(title='Selected File', message='Done!')


if __name__ == "__main__":
    app = App()
    app.mainloop()