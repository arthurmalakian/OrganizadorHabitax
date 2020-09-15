from Utils import Utils
dir = "<pasta onde as pastas das quadras se encontram>"
pasta = "<pasta da quadra>"
if __name__ == '__main__':
    dirObj = Utils(dir+pasta)
    #comentar e descomentar de acordo com a necessidade
    dirObj.RemoveFilesPrefix()
    dirObj.RemoveFilesSufix()
    dirObj.CreateDirAndMove()