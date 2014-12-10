#coding:utf8

from azure.storage import TableService, Entity

class CustomerTable:

    def __init__(self):
        self.table_service = TableService(account_name='portalvhdspbrd34f2fnbl',account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')
    
    def insert(self,ID,Name,Country,City):
        task = {'PartitionKey': 'Customer', 
                'RowKey': ID, 
                'Name' : Name , 
                'Country' : Country,
                'City' : City}
	try:
            self.table_service.insert_entity('Customer', task)
	except:
	    print"azure.WindowsAzureConflictError: Customer Conflict"
    def listAll(self):
        tasks = self.table_service.query_entities('Customer', "PartitionKey eq 'Customer'")
	i=0
	for task in tasks:
            i=i+1
	    print("Name: %s, Country: %s, City: %s") %(task.Name,task.Country,task.City)
	print("Total Customer: %s") %(i)
