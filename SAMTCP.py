import socket


# The Server Class
class Server:
	
	def __init__(self, ip, port, bufferSize):
		self.ip = ip
		self.port = port
		self.bufferSize = bufferSize
		
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.bind((ip, port))
		self.s.listen(5)

		self.conn, addr = self.s.accept()
		print("Connection address: ", addr)
	
	def checkForMessage(self):
		self.data = self.conn.recv(self.bufferSize).decode('utf-8')
		if not self.data: 
			return False
		return True
	
	def getMessage(self):
		# print("received data: ", self.data)
		return(self.data)
		
	def sendMessage(self, message):
		self.conn.send(message.encode('utf-8'))
		return
		
	def closeConnection(self):
		self.s.close()
		

# Client Class
class Client:
	def __init__(self, ip, port, bufferSize):
		self.ip = ip
		self.port = port
		self.bufferSize = bufferSize
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((ip, port))
	
	def sendMessage(self, message):
		self.s.send(message.encode('utf-8'))
	
	def closeConnection(self):
		self.s.close()

	def checkForMessage(self):
		self.data = self.s.recv(self.bufferSize).decode('utf-8')
		if not self.data: 
			return False
		return True
	
	def getMessage(self):
		return(self.data)
		
	def checkConnection(self):
		self.sendMessage("Connected?")
