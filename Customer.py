#coding:utf8

class Customer:
    
    def __init__(self,ID, Name,Country,City):
        
        self.ID = ID
        self.Name = Name
        self.Country = Country
        self.City = City
        
    def getID(self):
        return self.ID
    
    def getName(self):
        return self.Name
    
    def getCountry(self):
        return self.Country
    
    def getCity(self):
        return self.City
