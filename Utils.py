import os
import shutil
from pathlib import Path

class Utils:
    def __init__(self, path):
        self.path = path
    #criar diretorio a partir do nome do arquivo e move-lo
    def CreateDirAndMove(self):
        for file in os.listdir(self.path):
            if not (os.path.isdir(self.path + file)):
                print("Creating directory for " + Path(self.path + file).stem+".pdf ...")
                os.mkdir(self.path + "Lote " + Path(self.path + file).stem)
                shutil.move(self.path + file, self.path + "Lote " + Path(self.path + file).stem)
    #remover prefixo "lote" em minusculo
    def RemoveFilesPrefix(self):
        for file in os.listdir(self.path):
            if not (os.path.isdir(self.path+file)):
                print("Old name: "+Path(self.path+file).stem)
                newstr = str.split(Path(self.path + file).stem," ",1)
                print("New Name: "+newstr[1])
                os.rename(self.path+file,self.path+newstr[1]+".pdf")
    #remover sufixo "-<numero_da_quadra>" dos arquivos
    def RemoveFilesSufix(self):
        for file in os.listdir(self.path):
            if not (os.path.isdir(self.path+file)):
                print(Path(self.path+file).stem)
                newstr = str.split(Path(self.path + file).stem,"-")
                print(newstr[0])
                os.rename(self.path+file,self.path+newstr[0]+".pdf")
