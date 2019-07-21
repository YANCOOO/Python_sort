import queue
import threading
import time


flag =0


class myThread(threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name 
		self.q = q
	def run(self):
		print ("Start" + self.name)
		queue_ue(self.name,self.q)
		print ("end" + self.name)
		
def queue_ue(threadName, q):
	while not flag:
		queueLock.acquire()
		if not workQueue.empty():
			data = q.get()
			queueLock.release()
			print ("%s processing %s" % (threadName,data))
		else:
			queueLock.release()
		time.sleep(1)

threadList = ["td_01", "td_02", "td_03"]
nameList = ["1", "2", "3", "4", "5"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

for tName in threadList:
	thread = myThread(threadID, tName, workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1
    
queueLock.acquire()
for word in nameList:
	workQueue.put(word)
queueLock.release()

while not workQueue.empty():
	pass
	
flag = 1

for t in threads:
	t.join()
print ("Exit")
		

		
		
		
