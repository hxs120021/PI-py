from MainUI.MainUI import *
from MainUI.Draw import Draw
from NetSocket.SendMsg import SendMsg
from NetSocket.SendCheck import SendCheck
from NetSocket.WaitAlrm import WaitAlrm
from Sensor.Sensor import Sensor
from queue import Queue
sendQueue = Queue()
hostQueue = Queue()

#hostQueue.put("80^91^36")
#hostQueue.put("81^92^36.5")
#hostQueue.put("82^93^36.7")
#hostQueue.put("83^94^36.9")
#hostQueue.put("84^95^36.5")
#hostQueue.put("85^96^36.4")
#hostQueue.put("86^97^37")
#hostQueue.put("87^98^37.8")
#hostQueue.put("88^99^37.6")
#hostQueue.put("89^98^38")
#hostQueue.put("90^91^39")
#hostQueue.put("91^93^40")
#hostQueue.put("82^95^38.9")
#hostQueue.put("93^97^36.7")
#hostQueue.put("84^99^36")
#hostQueue.put("95^98^36")
#hostQueue.put("86^96^36")
#hostQueue.put("97^94^36")
#hostQueue.put("88^92^36")
#hostQueue.put("99^90^36")
#hostQueue.put("86^99^36")
#hostQueue.put("90^99^36")


equ = "ICU001^equ001^testname^man^40"
sendIP = "10.63.2.115"
bindip = "10.63.10.72"

def start_button(even):
	#ok

	#no
	sensor = Sensor(sendQueue, hostQueue)
	sensor.getData()
	#ok
	sendcheck = SendCheck(sendQueue, sendIP)
	sendcheck.whilesend()
	waitalrm = WaitAlrm(bindip)
	waitalrm.wait()
	draw = Draw([hr_can, spo2_can, temp_can], [bid_lb, sid_lb, name_lb, sex_lb, age_lb], hostQueue)
	draw.draw()
	pass

start_but.bind('<ButtonPress-1>', start_button)

def end_button(even):
	#hostQueue.put("80^91^36")
	exit()
	pass


end_but.bind('<ButtonPress-1>', end_button)

def alrm_button(even):
	#sendalrm = SendAlrm("127.0.0.1", 9988)
	#sendalrm.send("error")
	pass

alarm_but.bind('<ButtonPress-1>', alrm_button)

sendequ = SendMsg(sendIP, 6698, equ)
sendequ.send()
root.mainloop()
