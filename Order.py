#coding:utf8

class Order:
    
    def __init__(self,ID,CustomerID,ProductID,Datetime,TotalPrice):
        self.ID = ID
        self.CustomerID = CustomerID
        self.ProductID = ProductID
        self.Datetime = Datetime
        self.TotalPrice = TotalPrice
    def getID(self):
        return self.ID
    
    def getCustomerID(self):
        return self.CustomerID
    
    def getProductID(self):
        return self.ProductID
    
    def getDatetime(self):
        return self.Datetime
    
    def getTotalPrice(self):
        return self.TotalPrice
