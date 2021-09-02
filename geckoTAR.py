from tkinter import *
from tkinter.filedialog import *
import tarfile



def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.style="Helvetica 13 bold italic" # font des nombres écrits sur la grille
        self.title("GeckoTAR - Romulus Edition")
        Label(self,font=self.style,text="GeckoTAR - Romulus Edition").pack()
        fen=Canvas(self,width="400",height="140")
        photo = PhotoImage(file= "version.dat")
        fen.create_image(200,50,image=photo)
        fen.pack()
        baide=Button(self,width=15,text="Choisir fichier",font=self.style,command=self.formater)
        baide.pack()
        bb=Button(self,width=15,text="Choisir dossier",font=self.style,command=self.formaterdoc)
        bb.pack()
        self.mainloop()

    def formater(self):
        t=askopenfilename()
        make_tarfile(t+".tar.gz",t)

    def formaterdoc(self):
        t=askdirectory()
        make_tarfile(t+".tar.gz",t)
        
        
        
    
        

Application()
