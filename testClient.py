import SAMTCP as s

# Init Connection
client = s.Client('127.0.0.1', 5005, 20)

# Send check connection message
client.checkConnection()

# Look for messages and print results	
while 1:
	if client.checkForMessage():
		print(client.getMessage())
	client.sendMessage('I am the Client')