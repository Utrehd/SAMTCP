import SAMTCP as s

# Init Connection
server = s.Server('127.0.0.1', 5005, 20)

# Look for messages and print results		
while 1:
	if server.checkForMessage():
		print(server.getMessage())
		server.sendMessage('Ja Hallo du')
conn.close