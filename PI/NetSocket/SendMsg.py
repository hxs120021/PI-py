import socket
from Task.BaseThread import BaseThread

#发送报警，发送设备信息
class SendMsg:
	def __init__(self, ip, port, message):
		self.ip = ip
		self.port = port
		self.message = message
		
	def send(self):
		task = BaseThread(self.func)
		task.start()

	def func(self):
		print("start send Msg")
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((self.ip, self.port))
		client.send(self.message.encode("utf-8"))
		msg = client.recv(1024)
		client.close()

	