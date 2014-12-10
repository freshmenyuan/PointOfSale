#coding:utf8

from azure.storage import TableService, Entity
import json

class OrderTable:

    def __init__(self):
        self.table_service = TableService(account_name='portalvhdspbrd34f2fnbl', 
                                          account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')

    def insert(self,ID,CustomerID,ProductID,Datetime,TotalPrice):
        task = {'PartitionKey': 'Order',
                'RowKey': ID,
                'CustomerID' : CustomerID,
                'ProductID' : ProductID,
                'Datetime' : Datetime,
                'TotalPrice' : TotalPrice}
        try:
            self.table_service.insert_entity('Order', task)
        except:
            print"azure.WindowsAzureConflictError: Order Conflict"
        

    def listAll(self):
        task1 = self.table_service.query_entities('Order', None, None, 1000)
	task2 = self.table_service.query_entities('Order', None, None, 1000,
						  task1.x_ms_continuation['NextPartitionKey'],
						  task1.x_ms_continuation['NextRowKey'])
        task3 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task2.x_ms_continuation['NextPartitionKey'],
                                                  task2.x_ms_continuation['NextRowKey'])
	task4 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task3.x_ms_continuation['NextPartitionKey'],
                                                  task3.x_ms_continuation['NextRowKey'])
	'''
	task5 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task4.x_ms_continuation['NextPartitionKey'],
                                                  task4.x_ms_continuation['NextRowKey'])
	task6 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task5.x_ms_continuation['NextPartitionKey'],
                                                  task5.x_ms_continuation['NextRowKey'])
	task7 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task6.x_ms_continuation['NextPartitionKey'],
                                                  task6.x_ms_continuation['NextRowKey'])
	task8 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task7.x_ms_continuation['NextPartitionKey'],
                                                  task7.x_ms_continuation['NextRowKey'])
	task9 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task8.x_ms_continuation['NextPartitionKey'],
                                                  task8.x_ms_continuation['NextRowKey'])
	task10 = self.table_service.query_entities('Order', None, None, 1000,
                                                  task9.x_ms_continuation['NextPartitionKey'],
                                                  task9.x_ms_continuation['NextRowKey'])
	'''
	i=0
	for task in task1:
	    i=i+1
	    '''
            print("ID: %s, CustomerID: %s, ProductID: %s, Datetime: %s, TotalPrice: %s") %(task.RowKey,
	              task.CustomerID,task.ProductID,task.Datetime,task.TotalPrice)
      	    '''
	    print(task.TotalPrice)      
        for task in task2:
            i=i+1
            print(task.TotalPrice)
	print("Total Order: %s") %(i)
    
    def TableInfo(self):
	info=self.table_service.query_tables()
        for i in info:
            print(i.name)
