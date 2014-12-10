#coding:utf8
import json
import urllib2
from azure.storage import TableService, Entity

class Iterator:
    def __init__(self,table):
        self.DataCollector = []
        self.i=0
	self.Table=table
        self.table_service = TableService(account_name='portalvhdspbrd34f2fnbl',                       
account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')
        self.task = self.table_service.query_entities(self.Table, None, None, 100)
        
	if table=="Customer":
	    self.i=self.i+100
	    print(self.i)
	    for line in self.task:
	        self.DataCollector.append({'ID': line.RowKey,
                		           'Name' : line.Name ,
                                           'Country' : line.Country,
                                           'City' : line.City})
            self.iteratorCustomer(self.task)

	if table=="Order":
	    self.i=self.i+100
            print(self.i)
	    for line in self.task:
	        self.DataCollector.append({'ID': line.RowKey,
                    			   'CustomerID' : line.CustomerID,
                     			   'ProductID' : line.ProductID,
                    			   'Datetime' : line.Datetime,
                    			   'TotalPrice' : line.TotalPrice})
            self.iteratorOrder(self.task)
     
    def iteratorCustomer(self,task):
        try:
            data = self.table_service.query_entities(self.Table, None, None, 100,
                                                  task.x_ms_continuation['NextPartitionKey'],
                                                  task.x_ms_continuation['NextRowKey'])
            self.i=self.i+len(data)
	    print(self.i)
	    for line in data:
	        self.DataCollector.append({'ID': line.RowKey,
                                       	   'Name' : line.Name ,
                                           'Country' : line.Country,
                                           'City' : line.City})
	    self.iteratorCustomer(data)
        except:
	    pass

    def iteratorOrder(self,task):
        try:
            data = self.table_service.query_entities(self.Table, None, None, 100,
                                                  task.x_ms_continuation['NextPartitionKey'],
                                                  task.x_ms_continuation['NextRowKey'])
            self.i=self.i+len(data)
            print(self.i)
            for line in data:
                self.DataCollector.append({'ID': line.RowKey,
                                           'CustomerID' : line.CustomerID,
                                           'ProductID' : line.ProductID,
                                           'Datetime' : line.Datetime,
                                           'TotalPrice' : line.TotalPrice})
            self.iteratorOrder(data)
        except:
            pass

    def getDatas(self):
        return self.DataCollector
