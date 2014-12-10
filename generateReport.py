#coding:utf8
import json,datetime
from Iterator import Iterator
from azure.storage import TableService, Entity

class Report():

    def __init__(self):
	self.orders = Iterator("Order").getDatas()
        self.customers = Iterator("Customer").getDatas()
	self.countrys = [{"Country":"Country","TotalPrice":1,"CustomerNumber":1}]
	self.ReportA()
	self.ReportB()
	self.ReportC()

    def ReportA(self):
        countrys=self.countrys
        orders=self.orders
	customers=self.customers

        for order in orders:
            for customer in customers:
                '''find a order match to a customers'''
                if customer.get("ID")==order.get("CustomerID"):
               
                    for i in range(len(countrys)):

                        if countrys[i].get("Country")==customer.get("Country"):
                            countrys[i]={"Country":customer.get("Country"),
                                         "TotalPrice":countrys[i].get("TotalPrice")+order.get("TotalPrice"),
					 "CustomerNumber":countrys[i].get("CustomerNumber")+1}
		            break
		        elif i==(len(countrys)-1):
                            countrys.append({"Country":customer.get("Country"),
                                             "TotalPrice":order.get("TotalPrice"),
					     "CustomerNumber":1})  
	    		    break
		        else:
			    pass
	        else:
		    pass      
	self.countrys=countrys           
	for line in countrys:
	    self.writeToFile(line,"ReportA.txt")

    def ReportB(self):
	orders=self.orders
        customers=self.customers
	countrys=self.countrys

	for line in countrys:
	    mean = {"Country":line.get("Country"),
		    "AverageOrderPrice":line.get("TotalPrice")/line.get("CustomerNumber")}
	    self.writeToFile(mean,"ReportB.txt")
	
    def ReportC(self):
	orders=self.orders
        customers=self.customers
	
	LastSevenDaysOrder = []
	
	for order in orders:
	    date_object = datetime.datetime.strptime(order.get("Datetime"), "%Y-%m-%d %H:%M:%S.%f")
	    now= datetime.datetime.now()
	    days=now-date_object
	    
	    if days.days <= 7:
		LastSevenDaysOrder.append(order)

	for order in LastSevenDaysOrder:
	    for customer in customers:
		if customer.get("ID")==order.get("CustomerID"):
		    data={"OrderID":order.get("ID"),
			  "CustomerName":customer.get("Name"),
			  "Country":customer.get("Country"),
			  "City":customer.get("City"),
			  "DateTime":order.get("Datetime"),
			  "TotalPrice":order.get("TotalPrice")}
		    self.writeToFile(data,"ReportC.txt")


    def writeToFile(self,data,fileName):
        with open(fileName, 'a') as outfile:
            json.dump(data, outfile)
            outfile.write('\n')
