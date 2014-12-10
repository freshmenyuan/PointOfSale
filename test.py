#coding:utf8

from azure.storage import TableService, Entity
from CustomerTable import CustomerTable
from OrderTable import OrderTable 
from Iterator import Iterator
from generateReport import Report
#table_service = 
#TableService(account_name='portalvhdspbrd34f2fnbl',account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')

#tasks = table_service.query_entities('Customer', "PartitionKey eq 'Customer'")
#print(len(tasks))

#table_service.delete_entity('Customer', 'Customer', '001')
#CustomerTable().insert("test","test","test","test")
#CustomerTable().listAll()
#OrderTable().listAll()
#OrderTable().TableInfo()
#print (len(Iterator("Customer").getDatas()))
Report()
