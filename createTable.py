#coding:utf8

from azure.storage import TableService, Entity 

table_service = TableService(account_name='portalvhdspbrd34f2fnbl',
account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')

table_service.create_table('Customer')

table_service.create_table('Order')
