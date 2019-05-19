import socket
from Task.BaseThread import BaseThread
from queue import Queue

#发送检测的数据
class SendCheck(object):

	def __init__(self,queue, ip):
		self.queue = queue
		self.ip = ip

	def whilesend(self):
		sendThread = BaseThread(self.func)
		sendThread.start()

	def func(self):
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((self.ip, 9966))
		while(True):
			try:
				checkdata = self.queue.get()
				client.send(checkdata.encode("utf-8"))
			except ConnectionError as e:
				print(str(e))
				break
		client.close()