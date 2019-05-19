from Task.BaseThread import BaseThread
from MainUI.Port import Port

class Draw(object):
	def __init__(self, canvas, lables, queue):
		self.canvas = canvas
		self.lables = lables
		self.queue = queue

	def draw(self):
		drawThread = BaseThread(self.DrawGraph)
		drawThread.start()

	def DrawGraph(self):
		oldHrPort = Port(2, 89)
		oldSpo2Port = Port(2, 89)
		oldTempPort = Port(2, 89)

		i = 0
		while(True):
			data  = self.queue.get()
			strsp = data.split('^')

			hr = int(strsp[0])
			spo2 = float(strsp[1])
			temp = float(strsp[2])

			self.lables[0]["text"] = str(hr)
			self.lables[1]["text"] = str(spo2)
			self.lables[2]["text"] = str(temp)

			newHrPort = Port(i*10+5, self.GetHrPx(hr))
			newSpo2Port = Port(i*10+5, self.GetSpo2Px(spo2))
			newTempPort = Port(i*10+5, self.GetTempPx(temp))

			self.canvas[0].create_line(oldHrPort.x, oldHrPort.y, newHrPort.x, newHrPort.y)
			self.canvas[1].create_line(oldSpo2Port.x, oldSpo2Port.y, newSpo2Port.x, newSpo2Port.y)
			self.canvas[2].create_line(oldTempPort.x, oldTempPort.y, newTempPort.x, newTempPort.y)

			oldHrPort = newHrPort
			oldSpo2Port = newSpo2Port
			oldTempPort = newTempPort

			if(i == 30):
				oldHrPort.clear()
				self.canvas[0].delete("all")
				oldSpo2Port.clear()
				self.canvas[1].delete("all")
				oldTempPort.clear()
				self.canvas[2].delete("all")
				i = 0
			i = i + 1

	def GetHrPx(self, hr):
		px = 90-(3/5)*hr
		return int(px)
	
	def GetSpo2Px(self, spo2):
		px = 3.6*(100-spo2)
		return int(px)

	def GetTempPx(self, temp):
		px = 4.5*(52-temp);
		return int(px)