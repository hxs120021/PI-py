from Task.BaseThread import BaseThread
import socket

class WaitAlrm(object):
	def __init__(self, ip):
		self.ip = ip
		pass

	def wait(self):
		waitThread = BaseThread(self.func)
		waitThread.start()

	def func(self):
		print("wait alrm")
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((self.ip, 9970))
		server.listen(10)
		while(True):
			conn, addr = server.accept()
			try:
				data = conn.recv(1024)
				data = data.decode("utf-8")
				print(data + "报警")
				conn.send("bbbjjj".encode("utf-8"))
			except ConnectionResetError as e:
				print("have error, in except")

			conn.close()