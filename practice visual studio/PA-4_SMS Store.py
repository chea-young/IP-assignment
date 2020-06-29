"""
Create a new class, SMS_store. The class will instantiate SMS_store objects, similar to an inbox or outbox on a cellphone:

my_inbox = SMS_store()
This store can hold multiple SMS messages (i.e. its internal state will just be a list of messages). 
Each message will be represented as a tuple:

(has_been_viewed, from_number, time_arrived, text_of_SMS)
The inbox object should provide these methods:

my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
  # Makes new SMS tuple, inserts it after other messages
  # in the store. When creating this message, its
  # has_been_viewed status is set False.

my_inbox.message_count()
  # Returns the number of sms messages in my_inbox

my_inbox.get_unread_indexes()
  # Returns list of indexes of all not-yet-viewed SMS messages

my_inbox.get_message(i)
  # Return (from_number, time_arrived, text_of_sms) for message[i]
  # Also change its state to "has been viewed".
  # If there is no message at position i, return None

my_inbox.delete(i)     # Delete the message at index i
my_inbox.clear()       # Delete all messages from inbox
Write the class, create a message store object, write tests for these methods, and implement the methods.
"""
import time

class SMS_store():
    def __init__(self, *newmessage):
        self.messages = []
        if(newmessage != False):
            self.messages.append(newmessage)
        
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS,read = False):
        self.messages.append((from_number, time_arrived, text_of_SMS, read))
        
    def message_count(self):
        return len(self.messages)
    
    def get_unread_indexes(self):
        list = [i for i in range(len(self.messages)) if(self.messages[i][3] == False)]
        return list
    
    def get_message(self, i):
        try:
            self.messages[i] = (self.messages[i][0], self.messages[i][1], self.messages[i][2],True)
            return (self.messages[i][0], self.messages[i][1], self.messages[i][2])
        except IndexError as err:
            print(err)
            return None
    
    def delete(self, i):
        try:
            del self.messages[i]
        except :
            print("There isn't a message")
            
    def clear(self):
        self.messages = []
        
time_stamp = time.time()
r1 = SMS_store( '010-1234-5678', time.ctime(time_stamp), 'Hello', False)
time.sleep(3)
time_stamp = time.time()
r1.add_new_arrival('010-4567-8913', time.ctime(time_stamp), 'Hi')
time.sleep(5)
time_stamp = time.time()
r1.add_new_arrival('010-6546-6565', time.ctime(time_stamp), 'Bye')
print('The number of messages : ',r1.message_count())
print('Unread messages : ', r1.get_unread_indexes())
print("Third messages: ", r1.get_message(2))
print("4th messages: ", r1.get_message(3))
print('Unread messages : ',r1.get_unread_indexes())
r1.delete(5)
r1.delete(1)
print('The number of messages after delete: ', r1.message_count())
r1.clear()
print('The number of messages after clear : ', r1.message_count())