from Media import Media
class Film(Media):
    def __init__(self,iD=None,name=None,director=None,IMDB=None,url=None,duration=None,casts=None):
        Media.__init__(self,iD,name,director,IMDB,url,duration,casts)
    
    