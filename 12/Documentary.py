from Media import Media
class Documentary(Media):
    def __init__(self,iD,name,director,IMDB,url,duration,casts,parts):
        Media.__init__(self,iD,name,director,IMDB,url,duration,casts)
        self.parts=parts
    
    def showInfo(self):
        print(str(self.id)+'\t'+self.name+'\t'+self.director+'\t'+str(self.IMDB)+'\t'+str(self.duration)+'\t\t'+self.casts+'\t'+str(self.parts))
