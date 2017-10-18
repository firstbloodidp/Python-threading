#!/usr/bin/python3

import hashlib
import threading
import time
import config

#findFlag = 0
#result = 0

myPassword = '12DC4DB5B4636DD86F46C138B2EE0386CC1C5C5FBCF5ED302B3144869D9E500B'
myPassword = myPassword.lower()

#12DC4DB5B4636DD86F46C138B2EE0386CC1C5C5FBCF5ED302B3144869D9E500B
#72D96D46543F3B7A9765B96007683315D328C94579B98FDAB4F70F9E47013319 - 19000000 FOR TESTING

class myThread (threading.Thread):
   def __init__(self, threadID, name, startNumber, endNumber):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.startNumber = startNumber
      self.endNumber = endNumber

   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      rangeSha256(self.startNumber, self.endNumber, self.name)
      # Free lock to release next thread
      threadLock.release()

def rangeSha256 (startNumber,endNumber,threadName):
   for i in range(startNumber-1,endNumber):
      a =  hashlib.sha256(bytes(str(i), encoding='utf-8')).hexdigest()
      if i % 1000000 == 0:
         print (" %s %s: %s" % (threadName, time.ctime(time.time()),i))
      if a == myPassword or config.findFlag == 1:
         if config.findFlag == 1:
            print ("Stoping  %s" % (threadName))
            break
         config.result = i
         print ("Stoping  %s" % (threadName))
         config.findFlag = 1
         break


threadLock = threading.Lock()
threads = []

for i in range(1,43):
   startNumber = round(float(10000000) + float(i - 1) * (float(89999999) / float(42)))
   endNumber = round(float(10000000) + float(i) * (float(89999999) / float(42)))

   # Create new threads
   name = "Thread-"+ str(i)
   threads.append(myThread(i, name, startNumber, endNumber))

   # Start new Threads
   threads[i-1].start()

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")

print (config.result)