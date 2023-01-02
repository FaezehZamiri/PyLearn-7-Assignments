from pytube import YouTube
class Media():
    def __init__(self,iD=None,name=None,director=None,IMDB=None,url=None,duration=None,casts=None):
        self.id=iD
        self.name=name
        self.director=director
        self.IMDB=IMDB
        self.url=url
        self.duration=duration
        self.casts=casts

    def showInfo(self):
        print(str(self.id)+'\t'+self.name+'\t'+self.director+'\t'+str(self.IMDB)+'\t'+str(self.duration)+'\t\t'+str(self.casts))
    
    def download(self):  
        url=self.url
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

    def showMainMenu(self):
        print("1-Film")
        print("2-Clip")
        print("3-Serial")
        print("4-Documentary")
        print("5-Exit")

