from Media import Media
class Clip(Media):
    def __init__(self,iD,name,director,IMDB,url,duration,casts):
        Media.__init__(self,iD,name,director,IMDB,url,duration,casts)

    