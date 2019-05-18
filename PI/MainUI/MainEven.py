#from MainUI.MainUI import MainUI
#from MainUI.Draw import Draw
#from NetSocket.SendAlrm import SendAlrm
#import SendCheck
#import WaitAlrm
#from Sensor import Sensor
#from queue import Queue
#sendQueue = Queue()
#hostQueue = Queue()

#equ = "ICU001^equ001^testname^man^40"

#def start_button():
#	sendequ = SendAlrm("127.0.0.1", 6698)
#	sendequ.send(equ)
#	sensor = Sensor(sendQueue, hostQueue)
#	sensor.getData()
#	sendcheck = SendCheck(sendQueue)
#	sendcheck.whilesend()
#	waitalrm = WaitAlrm()
#	waitalrm.wait()
#	draw = Draw([hr_can, spo2_can, temp_can], [bid_lb, sid_lb, name_lb, sex_lb, age_lb], hostQueue)
#	draw.draw()
#	pass

#start_but.bind('<ButtonPress-1>', start_button)

#def end_button():
#	exit()

#end_but.bind('<ButtonPress-1>', end_button)

#def alrm_button():
#	sendalrm = SendAlrm("127.0.0.1", 9988)
#	sendalrm.send("error")

#alarm_but.bind('<ButtonPress-1>', alrm_button)