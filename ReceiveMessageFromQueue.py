#coding:utf8

from azure.storage import QueueService
from azure.servicebus import ServiceBusService, Message, Queue
class ReceiveMessage:

    def __init__(self):
	self.messages = None

    def message(self):

	try:
	    queue_service = QueueService(account_name='portalvhdspbrd34f2fnbl',account_key='y48JkXg+VcHQRCgsylJf4xV4Fd0AuJNkQKSwGhAR+BppHnFhkI+UHPOS/oYaTo0rqFCGQkEBW+thNFZNB9W8yg==')
            #queue_service.create_queue('taskqueue')
            self.messages = queue_service.get_messages('taskqueue')
            for message in messages:
                ''' print(message.message_text)'''
                self.queue_service.delete_message('taskqueue', message.message_id, message.pop_receipt)
	except:
	    pass

        return self.messages
