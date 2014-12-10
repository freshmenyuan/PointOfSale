#coding: utf8

from ReceiveMessageFromQueue import ReceiveMessage
from thread import start_new
from CustomerTable import CustomerTable
from OrderTable import OrderTable
import time, json

def getMessage(delay):

    while True:

        messages = ReceiveMessage().message()
        
        for message in messages:
            data = json.loads(message.message_text)

            if data.get("What")=="Customer":
                CustomerTable().insert(data.get("ID"),
                                       data.get("Name"),
                                       data.get("Country"),
                                       data.get("City"))
	
            elif data.get("What")=="Order":
                OrderTable().insert(data.get("ID"),
				    data.get("CustomerID"),
				    data.get("ProductID"),
				    data.get("Datetime"),
				    data.get("TotalPrice"))
	   
	    print(data)
try:
    start_new(getMessage,(0.01,))
    #start_new(CustomerTable().listAll,())
except:
    print "Error: unable to start thread"
#OrderTable().listAll()
while 1:
    pass
