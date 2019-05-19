import time
from Task.BaseThread import BaseThread
from max30102.max30102 import MAX30102 as max30102
from max30102.hrcalc import *
from MLX90614.mlx90614 import MLX90614 as mlx90614

class Sensor(object):

	def __init__(self, sendQueue, hostQueue):
		self.sendQueue = sendQueue
		self.hostQueue = hostQueue
		self.thermometer_address = 0x5a
		self.thermometer = mlx90614(self.thermometer_address)
		self.m = max30102()

	def getGY906Data(self):
		return self.thermometer.get_obj_temp()

	def getMax30102Data(self):
		red, ir = self.m.read_sequential()
		result = calc_hr_and_spo2(ir[:100], red[:100])
		
		return result[0], result[2]

	def getDataTask(self):
		task = BaseThread(self.getData)
		task.start()

	def getData(self):
		while(True):
			hr, spo2 = self.getMax30102Data()
			temp = self.getGY906Data()
			msg = str(hr) + '^' + str(spo2) + '^' + str(temp)
			print(msg)
			self.sendQueue.put(msg)
			self.hostQueue.put(msg)