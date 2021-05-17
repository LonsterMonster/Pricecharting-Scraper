class VideoGame:
    def __init__(self, title, console, loosePrice, completePrice, newPrice, Genre, ReleaseDate, ESRBRating, Publisher, Developer, ModelNumber, DiscCount, PlayerCount, AlsoCompatibleOn, UPC, Description):
        self.title = title
        self.console = console
        self.loosePrice = loosePrice
        self.completePrice = completePrice
        self.newPrice = newPrice
        
        self.Genre = Genre
        self.ReleaseDate = ReleaseDate
        self.ESRBRating = ESRBRating
        self.Publisher = Publisher
        self.Developer = Developer
        self.ModelNumber = ModelNumber
        self.DiscCount = DiscCount
        self.PlayerCount = PlayerCount
        self.AlsoCompatibleOn = AlsoCompatibleOn
        self.UPC = UPC
        self.Description = Description         

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getConsole(self):
        return self.console
    def setConsole(self, console):
        self.console = console

    def getLoosePrice(self):
        return self.loosePrice
    def setLoosePrice(self, loosePrice):
        self.loosePrice = loosePrice

    def getCompletePrice(self):
        return self.completePrice
    def setCompletePrice(self, completePrice):
        self.completePrice = completePrice

    def getNewPrice(self):
        return self.newPrice
    def setNewPrice(self, newPrice):
        self.newPrice = newPrice
        
    def getGenre(self):
        return self.Genre
    def setGenre(self, Genre):
        self.Genre = Genre
        
    def getReleaseDate(self):
        return self.ReleaseDate
    def setReleaseDate(self, ReleaseDate):
        self.ReleaseDate = ReleaseDate
    
    def getESRBRating(self):
        return self.ESRBRating
    def setESRBRating(self, ESRBRating):
        self.ESRBRating = ESRBRating
    
    def getPublisher(self):
        return self.Publisher
    def setPublisher(self, Publisher):
        self.Publisher = Publisher

    def getDeveloper(self):
        return self.Developer
    def setDeveloper(self, Developer):
        self.Developer = Developer

    def getModelNumber(self):
        return self.ModelNumber
    def setModelNumber(self, ModelNumber):
        self.ModelNumber = ModelNumber

    def getDiscCount(self):
        return self.DiscCount
    def setDiscCount(self, DiscCount):
        self.DiscCount = DiscCount

    def getPlayerCount(self):
        return self.PlayerCount
    def setPlayerCount(self, PlayerCount):
        self.PlayerCount = PlayerCount

    def getAlsoCompatibleOn(self):
        return self.AlsoCompatibleOn
    def setAlsoCompatibleOn(self, AlsoCompatibleOn):
        self.AlsoCompatibleOn = AlsoCompatibleOn    


    def getUPC(self):
        return self.UPC
    def setUPC(self, UPC):
        self.UPC = UPC
    
    def getDescription(self):
        return self.Description
    def setDescription(self, Description):
        self.Description = Description
        
    def printVals(self):
        print ("Title: {}\nConsole: {}\nLoose: ${}\nComplete: ${}\nNew: ${}\nGenre: ${}\nReleaseDate: ${}\nESRBRating: ${}\nPublisher: ${}\nDeveloper: ${}\nModelNumber: ${}\nDiscCount: ${}\nPlayerCount: ${}\nAlsoCompatibleOn: ${}\nUPC: ${}\nDescription: ${}\n".format(self.title, self.console, self.loosePrice, self.completePrice, self.newPrice))

