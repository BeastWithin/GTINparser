import datetime
from pystrich import datamatrix

class GTIN:
    #01 08699730540126 21 123936 17 160825 10 14002    naze
    #01 08699717010109 21 70634714 17 200730 10 151701 parol
    #01 barkod 21 sıra nu 17 y/a/g 10 seri nu
    def __init__(self,datamatrix):
        self.datamatrix=datamatrix
        parçalıkk = datamatrix.split("\x1d")   # telefondaki barkod okuyucunun verdiği kare şekli \x1d imiş. yani 29 muş ne demekse.
        self.barkod = parçalıkk[1][2:16]
        self.sıranu = parçalıkk[1][18:]
        self.yılaygün = parçalıkk[2][2:8]
        self.serinu = parçalıkk[2][10:]
        self.SKT = datetime.datetime( 
            int("20"+self.yılaygün[0:2]),
            int(self.yılaygün[2:4]),
            int(self.yılaygün[4:6])
            ) # "20"+   yazmamın nedeni yıl formatını 01.01.16 dan 01.01.2016 ya çevirmek
                                            
        
        #kare = lambda datamatrix : [i for i in datamatrix if not i.isnumeric()]   denemeydi

        
        
        #010869971701010921706347141720073010151701   telefondaki barkod okuyucunun verdiği şey
        #010869973054012621123936171608251014002
        
    def bas(self,dosya):
        dmenc=datamatrix.DataMatrixEncoder(self.datamatrix)
        dmenc.save(dosya)
