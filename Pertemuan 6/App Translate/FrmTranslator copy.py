from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("600x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Masukkan teks:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='English:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Sundanese:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Japanese:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=0, column=1, columnspan=3, padx=3, pady=3)

        self.txtHasil1 = Entry(mainFrame, width=50) 
        self.txtHasil1.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        self.txtHasil2 = Entry(mainFrame, width=50) 
        self.txtHasil2.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

        self.txtHasil3 = Entry(mainFrame, width=50) 
        self.txtHasil3.grid(row=4, column=1, columnspan=3, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate to English!',
            command=self.onTranslate1)
        self.btnTranslate.grid(row=1, column=1, padx=5, pady=5)

        self.btnTranslate = Button(mainFrame, text='Translate to Sundanese!',
            command=self.onTranslate2)
        self.btnTranslate.grid(row=1, column=2, padx=3, pady=3)

        self.btnTranslate = Button(mainFrame, text='Translate to Japanese!',
            command=self.onTranslate3)
        self.btnTranslate.grid(row=1, column=3, padx=3, pady=3)   

    def onTranslate1(self):
        # membuat instance object
        penterjemah = Translator()

        # menterjemahkan
        hasil1 = penterjemah.translate(self.txtSumber.get(), src='id', dest='en')  
       
        # menampilkan hasil terjemahan
        self.txtHasil1.insert(END,hasil1.text)
        

    def onTranslate2(self):
        # membuat instance object
        penterjemah = Translator()

        hasil2 = penterjemah.translate(self.txtSumber.get(), src='id', dest='su')

        self.txtHasil2.insert(END,hasil2.text)

    def onTranslate3(self):
        # membuat instance object
        penterjemah = Translator()

        hasil3 = penterjemah.translate(self.txtSumber.get(), src='id', dest='ja')
        self.txtHasil3.insert(END,hasil3.text)


    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 