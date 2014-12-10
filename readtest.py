#coding:utf8

from azure.storage import TableService, Entity

table_service = TableService(account_name='portalvhdspbrd34f2fnbl', 
account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')

task = table_service.get_entity('tasktable', 'tasksSeattle', '1')
print(task.description)
print(task.priority)
